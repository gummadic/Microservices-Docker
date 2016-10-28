# Description

This repository is an extension to https://github.com/Cogniteinc/devops-exercise. Here, an approach has been adopted by using tools such as Docker, Docker-Compose, Nginx, Flask, HAProxy and MongoDB to automate a development environment that could easily be scaled, deployed and maintained.

In this project, docker-compose is configured to compose, build and link necessary pre-build images such as tutum/HAProxy, tutum/nginx, mongodb and flask based auth and data microservices to automate the solution with minimal deployment tasks. Further, purpose of each image and service is explained below.

* HAProxy : To perform the load balancing on the micro-services.
* Nginx   : It acts as a reverse-proxy for both auth and data services
* Auth service : This microservice will create a user and assigns a token for authentication purpose.
* Data service : This microservice will fetch data from MongoDB for only authenticated requests.
* MongoDB : It acts as a document based data store for both auth and data microservices



# Steps to replicate in development environment.


Step 1: Clone this repository.


Step 2: Once cloned, cd to the directory where the code resides. To learn about what the code does, check here https://github.com/Cogniteinc/devops-exercise

Step 3: Follow the commands below to setup the development environment.

* docker-compose build
* docker-compose up
* docker-compose logs # to see the logs

# Auth Service
* http://0.0.0.0/api/auth/health
* http://0.0.0.0/api/auth/create     # To create a new user
* Once succesfully created, above web page will redirect to token web page for example: http://0.0.0.0/api/auth/token?key=chandu&secret=chandu

# Data Service
* http://0.0.0.0/api/data/health
* [GET/POST] http://0.0.0.0/api/data/accounts
  HEADERS
  token=12398472895nfewnrfjkwerfn203r2h4895ry3y498th3843t04











