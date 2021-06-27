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
git clone https://github.com/edith59/analytics-project-jupyter.git
```

2. Run docker-compose file

```console
docker-compose up --build
```
The root directory contains the `docker-compose.yaml` which
describes the configuration of service components. By executing following command
you will be able to run Dockerfiles for 2 containers (Python and SQL ones).

3. Access Jupyter Notebook

```console
datascience-notebook_1  |     To access the notebook, open this file in a browser:
datascience-notebook_1  |         file:///home/jovyan/.local/share/jupyter/runtime/nbserver-7-open.html
datascience-notebook_1  |     Or copy and paste one of these URLs:
datascience-notebook_1  |         http://26286bd7e857:8888/?token=XXXX
datascience-notebook_1  |      or http://127.0.0.1:8888/?token=XXXX
```

Once you run previously indicated command you should see links to access Jupyter Notebook as per the example above.
Access last URL : copy and paste into browser to access Jupyter stack.
Jupyter Notebook with data transformation operations will be available in /work folder.

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

### Dataset
Publicly available, non-commercial data set used for this project is available at the following link:
https://grouplens.org/datasets/movielens/latest/