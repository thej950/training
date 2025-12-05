# Dockerfile
 
  # this is my base image
```bash
FROM ubuntu

  # Add an instruction layer to the docker image use RUN Command

RUN apt update

RUN apt install apache2 -y

  # test.html is to be copied from my localhost to docker image

ADD test.html /var/www/html

  # as soon as container get started from the docker image then it runs the command

  # which is written in front of Entrypoint

ENTRYPOINT ["apachectl", "-D", "FOREGROUND"]

ENV name=DevOps
```

 
# 2nd Dockerfile for Copy and Add command

```bash
  #Base Image

FROM centos:7.4.1708

  #Create a directory in the image mydata

RUN mkdir /mydata

  # Copy myfiles (should be created under current folder ) in /mydata

COPY myfiles /mydata/myfiles

  # Copy myfile2 (should be created under current folder ) in /mydata

ADD myfile2 /mydata/myfile2

  # Download the file using ADD command and copy under /mydata

ADD https: dlcdn.apache.org/maven/maven-3/3.9.11/binaries/apache-maven-3.9.11-bin.tar.gz /mydata

  # ADD command will unzip the file and create under /mydata/maven dir

  # wget https: mirrors.estointernet.in/apache/maven/maven-3/3.6.3/source/apache-maven-3.6.3-src.tar.gz

ADD apache-maven-3.9.11-src.tar.gz /mydata/maven

 ```


# 3rd Dockerfile
 
FROM ubuntu

ENTRYPOINT echo "Hello World"
 
   29  # Dockerfile is the standard way to create the docker image from the script so whenever we are developing cicd pipeline then we need the automation script to develop the docker image and we use Dockerfile

   30  # Name is standard Dockerfile

   31  # Step 1 we need to choose the correct base docker image

   32  vi Dockerfile

   33  # command to build the docker image is docker build . -t webimg

   34  docker images

   35  docker ps -a

   36  docker rm -f c1 web

   37  docker ps -a

   38  docker rm -f web1

   39  # To delete all the images

   40  docker rmi -f $(docker ps -q)

   41  docker rmi -f $(docker images -q)

   42  docker images

   43  # lets build Dockerfile

   44  docker build . -t webimg

   45  docker images

   46  # To validate the image we will create a container from this image

   47  docker container run -it --name web -p 80:80 -d webimg

   48  docker ps -a

   49  docker logs web

   50  vi Dockerfile

   51  docker build . -t webimg

   52  docker ps -a

   53  docker rm web

   54  docker container run -it --name web -p 80:80 -d webimg

   55  docker ps

   56  docker ps -a

   57  docker logs web

   58  docker start web

   59  docker ps -a

   60  docker logs web

   61  cat Dockerfile

   62  vi Dockerfile

   63  docker build . -t webimg

   64  docker rm web

   65  docker container run -it --name web -p 80:80 -d webimg

   66  docker ps -a

   67  docker logs web

   68  cat Dockerfile

   69  vi Dockerfile

   70  docker build . -t webimg

   71  docker rm web

   72  docker container run -it --name web -p 80:80 -d webimg

   73  docker ps -a

   74  cat Dockerfile

   75  # Copy and Add Command...Both the commands are used to copy the files/folder from local host machine to docker image while building the dockerfile

   76  # Difference ADD is more advace as compare to Copy command

   77  rm Dockerfile

   78  touch myfiles myfile2

   79  ls

   80  wget https: dlcdn.apache.org/maven/maven-3/3.9.11/source/apache-maven-3.9.11-src.tar.gz

   81  nano Dockerfile

   82  docker build . -t img1

   83  docker images

   84  docker rmi -f $(docker images -f "dangaling=true" -q)

   85  docker rmi -f $(docker images -f "dangling=true -q)

   86  docker rmi -f $(docker images -f "dangling=true" -q)

   87  docker images

   88  docker rmi webimg

   89  docker rm -f web

   90  docker rmi webimg

   91  docker images

   92  docker container run -it --name c1 -d img1

   93  docker exec -it c1 ls

   94  docker exec -it c1 ls mydata

   95  docker exec -it c1 ls mydata/maven

   96  docker exec -it c1 ls mydata/maven/apache-maven-3.9.11

   97  cat Dockerfile

   98  rm Dockerfile

   99  nano Dockerfile

  100  docker build . -t img2

  101  docker run img2

  102  docker run img2 echo "Hello India"

  103  nano Dockerfile

  104  docker build . -t img3

  105  docker run img3

  106  docker run img3 echo "Hello India"

  107  cat Dockerfile



# Dockerfile without multistage
 
```bash
FROM maven

WORKDIR /

COPY src /src

COPY pom.xml /pom.xml

RUN mvn package

CMD java -cp /target/myproj-1.0-SNAPSHOT.jar com.raman.App

```

# Volume 

30  mkdir mydir
   31  docker container run -it --name c3 -v /home/ubuntu/mydir:/demo -d ubuntu
   32  docker inspect c3
   33  docker exec -it c3 ls /demo
   34  docker exec -it c3 touch /demo.java
   35  docker exec -it c3 ls /demo
   36  docker exec -it c3 touch /demo/demo.java
   37  docker exec -it c3 ls /demo
   38  ls mydir/
   39  docker rm -f c3
   40  ls mydir/


# Docker networking
 
  1  docker rm -f $(docker ps -aq)

    2  ip a

    3  docker container run -it --name c1 -d centos:7

    4  docker inspect c1

    5  docker container run -it --name c2 -d centos:7

    6  docker inspect c2

    7  docker exec -it c1 ping 172.17.0.3"

    8  docker exec -it c1 ping 172.17.0.3

    9  docker rm -f c1 c2

# we can define userdefined network bridge

   11  docker network --help

   12  docker network ls

   13  docker network create -d bridge webnetwork --subnet 192.168.0.0/16 --gateway 192.168.0.1

   14  docker network ls

   15  docker network inspect webnetwork

   16  docker container run -it --name c1 --network webnetwork -d centos:7

   17  docker inspect c1

   18  docker container run -it --name c2 --network webnetwork -d centos:7

   19  docker inspect c2

   20  docker exec -it c1 ping 192.168.0.3

   21  docker rm -f c1 c2

   22  docker network rm webnetwork

   23  docker network ls

   24  docker container run -it --name h1 --network host -d nginx

   25  docker rm -f h1

   26  # none network there is no ip address is assigned to container

   27  docker container run -it --name n1 --network none -d centos:7

   28  docker inspect n1

   29  docker network disconnect none n1

   30  docker network connect bridge n1

   31  docker inspect n1

 
# Compose 
cat compose.yaml

services:

   db:

     image: mysql:5.7

     volumes:

       - db_data:/var/lib/mysql

     restart: always

     environment:

       MYSQL_ROOT_PASSWORD: somewordpress

       MYSQL_DATABASE: wordpress

       MYSQL_USER: wordpress

       MYSQL_PASSWORD: wordpress
 
   wordpress:

     depends_on:

       - db

     image: wordpress:latest

     ports:

       - "8000:80"

     restart: always

     environment:

       WORDPRESS_DB_HOST: db:3306

       WORDPRESS_DB_USER: wordpress

       WORDPRESS_DB_PASSWORD: wordpress

       WORDPRESS_DB_NAME: wordpress

volumes:

    db_data: {}

 
  29  DOCKER_CONFIG=${DOCKER_CONFIG:-$HOME/.docker}

   30  mkdir -p $DOCKER_CONFIG/cli-plugins

   31  curl -SL https://github.com/docker/compose/releases/download/v2.19.0/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose

   32  chmod +x $DOCKER_CONFIG/cli-plugins/docker-compose

   33  docker compose version

   34  nano compose.yaml

   35  docker compose --help

   36  docker compose up -d

   37  docker ps -a

   38  docker inspect bb7f3749f5f1

   39  docker volume ls

   40  docker ps -a

   41  docker compose stop db

   42  docker ps -a

   43  docker compose start db

   44  docker ps -a

   45  docker compose down -v

   46  cat compose.yaml

 