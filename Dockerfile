FROM python:3.7.0
ADD . infosetDB
WORKDIR infosetDB
RUN pip3 install -r requirements.txt