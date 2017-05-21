FROM ubuntu:xenial
ADD . .
RUN apt-get update
RUN apt-get -y install sudo expect python3 python3-pip python3-dev memcached mariadb-server
RUN chmod -R a+rwx docker_scripts
RUN ./docker_scripts/secure_mysql.sh




CMD ["echo", "Running infoset-ng"]