# Launch Machine in AZ setup Docker 

apt update

apt install docker.io -y

docker --version

docker --help

docker images

docker image ls

docker pull ubuntu

docker images

docker container run -it --name c1 -d ubuntu

docker ps

# docker ps will show all the containers which are in running mode

docker container ls

# docker ps =docker container ls

# we can create the container with limited memory or cpu

docker container run -it --name web -d nginx

docker ps

docker stats web

docker container run -it --name web1 -m 8m -d nginx

docker stats web1

docker inspect web1

docker inspect web1 | grep Memory

docker container update web1 -m 16m

docker inspect web1 | grep Memory

docker container run -it --name web2 -c 410m -d nginx

docker container run -it --name web2 -c 410 -d nginx

docker inspect web2 | grep Cpu

docker exec -it c1 bash

docker exec -it c1 ls

docker stop c1

docker ps

docker ps -a

docker start c1

docker ps -a

# To stop the container forefully use kill command

docker kill c1

docker ps -a

docker restart c1

docker ps -a



# remove the container the docker rm, docker rm -f
docker ps -a
docker rm c1
docker stop c1
docker rm c1
docker rm web
docker rm -f web
docker ps -a
docker ps -aq
# remove all the containers
docker rm -f $(docker ps -a -q)
docker ps -a
docker images
docker rmi ubuntu
docker images
docker rmi nginx
docker images
# consider dev team has given the source code / build code to deply the application ainside the container
# let create a ubuntu container and install apache webserver and then copy my build code in the apache folder /var/www/html
docker container run -it --name web -p 80:80 -d ubuntu
docker ps
# to install apache inside the container
docker exec -it web apt update
docker exec -it web apt install apache2 -y
docker exec -it web service apache2 status
docker exec -it web service apache2 start
docker exec -it web ls /var/www/html
# let's create a simple html file which we consider as the code which we need to deploy inside the container so that my client can access the applicaiton
# docker cp command to copy the file from host machine to container
echo "<h1> This is super cool htkl file </h1>" > test.thml
docker cp test.thml web:/var/www/thml
docker cp test.thml web:/var/www/html
docker exec -it web ls /var/www/html
ls
mv test.thml test.html
docker cp test.html web:/var/www/html
curl localhost
curl localhost/test.html
docker ps
# we  cannot share the containers , but we can share the images
# lets create a docker imager(custom docker image) from the web container
# to create the docker image we need to use docker commit command
docker commit web webimg
# with above command new docker image webimg is created which has everything inside it as per web container
docker images
# now lets remove the container and create a new container from webimg
docker rm -f web
docker containe run -it --name web1 -p 80:80 -d webimg
docker container run -it --name web1 -p 80:80 -d webimg
docker ps
docker exec -it web service apache2 start
docker exec -it web1 service apache2 start


 
# how to share the images, 1. way to using docker hub (Cloud) public registry

# docker hub we need to create an account to push the images

# there are 2 types images we can store in docker hub 1 public (unlimited) 2. private (Paid plan from docker hub)

# lets login to docker hub through this terminal

docker login -u raman

docker login -u ramansharma95

# whenever we store the images on docuker hub we need to use a naming conventtion that the image name should be started with the dockerhub account userid means your image name lke userid/image name

# use image tag command to create another name of the image

docker images

docker image tag webimg ramansharma95/webimg1

docker images

docker push ramansharma95/webimg1

docker logout

docker login --help

docker login myreg987.azurecr.io -u myreg987

#now we are connected to azure container registry with the login server

# to push the image to acr we need to use the naming convention, image as loginserver/imagename

docker image tag webimg myreg987.azurecr.io/webimg

docker images

# now we can push the image to acr

docker push myreg987.azurecr.io/webimg

history

 