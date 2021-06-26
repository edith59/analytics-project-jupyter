<!--lint disable awesome-toc-->
## Getting started

These instructions will get you through the bootstrap phase of running
sample of containerized application with Docker Compose.

### Prerequisites

- Make sure that you have Docker and Docker Compose installed
  - Windows or macOS:
    [Install Docker Desktop](https://www.docker.com/get-started)
  - Linux: [Install Docker](https://www.docker.com/get-started) and then
    [Docker Compose](https://github.com/docker/compose)

### Running an application

1. Clone the repository
```console
git clone https://github.com/edith59/analytics-project.git
```

2. Run docker-compose file
The root directory contains the `docker-compose.yaml` which
describes the configuration of service components. By executing following command
you will be able to run Dockerfiles for 2 containers (Python and SQL ones).

```console
docker-compose up --build
```

### Stopping an application
To stop and remove all containers of the application run (alternatively use ctrl+c):

```console
docker-compose down
```

### Application output
Application output (result from data_transformation.py) will be showed automatically after you 
build you docker-compose file. 
For SQL container by default sql tables will be created and data from ml_latest_small
dataset will be loaded to them.
For analytics container by default python script will 
be invoked and results from queries will be presented. 


### Project directory structure
Overall:
Project incorporates 2 folders : analytics and database. Each of them has own Dockerfile.
In Dockerfile you define app’s environment so it can be reproduced anywhere.

Analytics container:
Apart from Dockerfile container incorporates requirements.txt file which has list of python libraries
needed to run python script. And python script itself available under data_transformation.py 
name.

Database container:
Apart from Dockerfile it incorporates dataset available under ml_latest_small folder
and queries folder that includes sql queries for creating tables and loading data into
them.

In root there is docker-compose file.
Thanks to docker-compose you can define and run multi-container Docker applications. 
With Compose, you use a YAML file to configure your application’s services. 
Then, with a single command, you create and start all the services from your configuration.

├── analytics/
│   ├── data_transformation.py   
│   ├── Dockerfile
│   └── requirements.txt
├── database/
│   ├── .dockerignore
│   ├── Dockerfile
│   ├── ml_latest_small/
│   │   ├── links.csv
│   │   ├── movies.csv
│   │   ├── ratings.csv
│   │   ├── README.txt
│   │   └── tags.csv
│   └── queries/
│       ├── create_tables.sql
│       └── load_data_to_tables.sql
├── docker-compose.yml
└── README.md