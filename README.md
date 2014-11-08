infrastructure
==============

This repo is for all backend infrastructure related code. We will start by installing docker and creating a docker image using the docker file in the docker directory. The docker file is a recipe to productionalize flask applications with nginx and uwsgi.

**Install Docker**

$ sudo apt-get update

$ sudo apt-get install docker.io

**Clone this repo**

$ git clone https://github.com/codeforpakistan/infrastructure.git

**Go to the docker directory**

$ cd infrastructure/docker/

**Build**

$ sudo docker build -t="arizqi/app:v1" .

**this will spit out an image id**

**Run**

$ sudo docker run -t -d -i <image_id>





