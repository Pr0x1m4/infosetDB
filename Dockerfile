FROM python:3
ADD . infosetDB
WORKDIR infosetDB
RUN apt-get update
RUN apt-get -y install python3 python3-pip python3-dev python3-setuptools
RUN pip3 install -r requirements.txt