FROM ubuntu:xenial
ADD . infoset-ng
RUN apt-get update
RUN apt-get -y install sudo expect python3 python3-pip python3-dev memcached
RUN useradd infoset -m 
RUN pip3 install --upgrade pip
USER infoset
CMD ["pip3", "install -r infoset-ng/requirements.txt"]
CMD ["python3", "/infoset-ng/bin/systemd/infoset-ng-api"]
CMD ["python3", "/infoset-ng/bin/systemd/infoset-ng-ingester"]
CMD ["python3", "/infoset-ng/bin/infoset-ng-cli"]
CMD ["echo", "Running infoset-ng"]