# Description

This repository is an extension to https://github.com/Cogniteinc/devops-exercise. Here, an approach has been adopted by using tools such as Docker, Docker-Compose, Nginx, Flask, HAProxy and MongoDB to automate a development environment that could easily be scaled, deployed and maintained.

In this project, docker-compose is configured to compose, build and link necessary pre-build images such as tatum/HAProxy, tatum/nginx, mongodb and flask based auth and data microservices to automate the solution with minimal deployment tasks. Further, purpose of each image and service is explained below.

* HAProxy : To perform the load balancing on the micro-services.
* Nginx   : It acts as a reverse-proxy for both auth and data services
* Auth service : This microservice will create an user and assigns a token for authentication purpose.
* Data service : This microservice will fetch data from MongoDB for only authenticated requests.
* MongoDB : It acts as a document based data store for both auth and data microservices



# Steps to replicate in development environment.


Step 1: Install boot2docker. Check here http://boot2docker.io/

Step 2: Run commands as mentioned below to setup boot2docker.

* boot2docker init
* boot2docker up
* eval "$(boot2docker shellinit)"
* boot2docker ip     # Later used to browse thru.

Step 3: Clone the repository as mentioned below.


Step 4: Once cloned, cd to the directory where the code resides. To learn about what the code does, check here https://github.com/Cogniteinc/devops-exercise

Step 5: Follow the commands below to setup the development environment.

* docker-compose build
* docker-compose up
* docker-compose logs # to see the logs

Step 6: Browse thru with the IP extracted from boot2docker and follow along as mentioned below to see how it works.

* http://192.168.59.104/api/auth/create     # To create a new user
* Once succesfully created, above web page will redirect to token web page for example: http://192.168.59.104/api/auth/token?key=chandu&secret=chandu
* [GET/POST] http://192.168.59.104/accounts
  HEADERS
  token=12398472895nfewnrfjkwerfn203r2h4895ry3y498th3843t04

  Note: IP used here i.e. 192.168.59.104 can be different in each and every machine. It depends on the 'boot2docker ip' output.










