FROM python:3.6
ADD . /infoset-ng
WORKDIR /infoset-ng
RUN pip3 install -r requirements.txt
EXPOSE 6000
CMD python /infoset-ng/docker/api.py
