import time
from pandas import DataFrame
from sqlalchemy import create_engine
import pandas as pd

db_name = 'database'
db_user = 'username'
db_pass = 'secret'
db_host = 'db'
db_port = '5432'


# Connect to the database
db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
db = create_engine(db_string)


def find_movies_nr():
    """
    Aim of this method is to find how many movies is present within dataset 'ml_latest_small'.
    As per readme.txt file "Each line of this file (movies.csv) after the header row represents one movie"
    :return number of movies in dataset, distinct number of titles, repeated titles if exist
    """
    # How many movies are in data set ?
    query_titles= "SELECT count(*) as cnt "\
                  "FROM movies"
    nr_movies = pd.read_sql_query(query_titles, db)

    # How many distinct titles ?
    query_titles= "SELECT count(distinct m.title) as cnt " \
                  "FROM movies m"
    nr_titles = pd.read_sql_query(query_titles, db)

    # How many distinct movie IDs ?
    query_movie_ids= "SELECT count(distinct m.movieId) as cnt "\
                     "FROM movies m"
    nr_movie_ids = pd.read_sql_query(query_movie_ids, db)

    # Check if dataset incorporates any repeated movie titles. If so, which of them are repeated ? 
    # As per readme.txt : "Errors and inconsistencies may exist in these titles." 
    repeated_titles_list = None
    if nr_movie_ids['cnt'][0] > nr_titles['cnt'][0]:
        query_repeated_titles= "SELECT m.title as title "\
                               "FROM movies m "\
                               "GROUP BY m.title "\
                               "HAVING COUNT(m.title) > 1 ;"
        df_repeated_titles = pd.read_sql_query(query_repeated_titles, db)
        repeated_titles_list = df_repeated_titles['title'].tolist()

    return nr_movies['cnt'][0], nr_titles['cnt'][0] , repeated_titles_list

def most_common_genre():
    """
    Aim of this method is to find out what is the most common genre of movie?
    :return most common genre of movie (string)
    """

    # Fetch movies table to pandas DataFrame
    df_movies = pd.read_sql_query("SELECT * "\
                                  "FROM movies ;", db)
    df_movies.rename(columns=df_movies.iloc[0])

    # Split genres column given pipe seperator
    split_genres = df_movies.genres.str.split('|')
    splitted_df = pd.DataFrame({'genres':split_genres.sum(),'title':df_movies.title.repeat(split_genres.str.len())})

    # Calculate which genre is the most common one
    common_genre = splitted_df['genres'].value_counts().idxmax()
    common_genre_nr = splitted_df['genres'].value_counts()[0]

    return common_genre, common_genre_nr

def top_rated_movies():
    """
    Aim of this method is to verify what are top 10 movies with highest rate ?
    :return pandas DataFrame with top 10 rated movies
    """

    query = "SELECT movies.movieid, title, count " \
            "FROM movies "\
            "JOIN (SELECT movieid, count(*) AS count "\
            "FROM ratings "\
            "WHERE rating = 5 "\
            "GROUP BY movieid "\
            "ORDER BY count "\
            "DESC LIMIT 10) t " \
            "ON movies.movieid = t.movieid ORDER BY 3 desc ; "

    # Fetch data from sql filtered to top 10 records with highest rate
    top_movies_df = pd.read_sql_query(query, db)

    return top_movies_df

def top_rated_users():
    """
    Aim of this method is to verify what are 5 most often rating users ?
    :return df of users that are most often rated together with number of made ratings
    """
    query = "SELECT r.userId, COUNT(r.userId) AS cnt "\
            "FROM ratings r "\
            "GROUP BY r.userId "\
            "ORDER BY cnt DESC "\
            "LIMIT 5;"
    
    # Fetch data from ratings table filtered as per requirement
    top_users_df = pd.read_sql_query(query, db)

    # Extract list of most often rating users
    top_users_list = top_users_df['userid'].tolist()

    return top_users_df

def run_first_and_last_rate():
    """
    Aim of this method is to find out when was done first and last rate included in data set
    and what was the rated movie title?
    :return first rate date, firstly rated movie title(s), last rate date, lastly rated movie title(s)
    """
    query = "SELECT r.timestamp as tmp, m.title, "\
            "'min' as level from ratings r "\
            "LEFT JOIN movies m on m.movieId=r.movieId "\
            "WHERE r.timestamp = (select min(r.timestamp) FROM ratings r) " \
            "UNION "\
            "SELECT r.timestamp as tmp, m.title, "\
            "'max' as level "\
            "FROM ratings r "\
            "LEFT JOIN movies m on m.movieId=r.movieId "\
            "WHERE r.timestamp = (select max(r.timestamp) from ratings r) ;"  

    # Fetch data from db including first and last rate date and corresponding movie title(s)
    ratings = pd.read_sql_query(query, db)

    # Limit DataFrame to have only rows related first rate date
    first_rated_df = ratings.loc[ratings['level'] == 'min']
    # Extract first available rate date
    first_rate_date = first_rated_df['tmp'][0]
    first_rate_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(first_rate_date))
    # Extract firstly rated movie title(s)
    first_rate_movies = first_rated_df['title'].tolist()

    # Limit DataFrame to have only rows related last rate date
    last_rated_df = ratings[ratings['level'] == 'max']
    # Extract last available rate date
    last_rate_date = last_rated_df['tmp'].tolist()[0]
    last_rate_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(last_rate_date))
    # Extract last rated movie title(s)
    last_rate_movies = last_rated_df['title'].tolist()

    return first_rate_date, first_rate_movies, last_rate_date, last_rate_movies

def movies_per_release_date():
    """
    Aim of this method is to find all movies released in 1990
    :return number of movies released in 1990 together with corresponding movie titles
    """

    query = "SELECT title as title "\
            "FROM movies "\
            "WHERE title ~* '(1990)';"

    # Fetch movies from db limited to these which have '1990' number within its title
    movies_filtered_per_release_date = pd.read_sql_query(query, db)
    movies_list = movies_filtered_per_release_date['title'].tolist()

    # Filter movies titles that have 1990 year present in parentheses as PostGreSQL omits them
    matching_titles = [title for title in movies_list if "(1990)" in title]

    # Count how many movies were released in 1990
    cnt_movies = len(matching_titles)
    return cnt_movies, matching_titles

if __name__ == '__main__':
    print('Application started')

    while True:
        print("Dataset has {} movies and {} distinct titles. Repeated movie titles are " \
              "{}".format(*find_movies_nr()))
        print("The most common genre is {}. It appears {} times.".format(*most_common_genre()))
        print("Top 10 rated movies are: {}".format(top_rated_movies()))
        print("Top 5 most often rating users: {}".format(top_rated_users()))
        print("First rating was made in {} and associated titles list that was found is {}, " \
              "Last rating was made in {} and associated titles list that was found is {}". \
              format(*run_first_and_last_rate()))
        print("Dataset incorporates of {} movies released in 1990. They are as follows: {}". \
              format(*movies_per_release_date()))
        
        time.sleep(5)
        break