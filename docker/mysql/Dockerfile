FROM mysql:latest
MAINTAINER me

ENV MYSQL_DATABASE=infoset \
    MYSQL_ROOT_PASSWORD=password

ADD infoset.sql /docker-entrypoint-initdb.d
