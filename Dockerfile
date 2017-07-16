FROM python:3
ADD . infoset-ng
RUN apt-get update
RUN apt-get -y install python3 python3-pip python3-dev python3-setuptools
WORKDIR infoset-ng
EXPOSE 6000
RUN pip3 install -r requirements.txt
CMD ["python3", "docker/api.py"]