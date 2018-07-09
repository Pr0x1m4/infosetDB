FROM python:3
ADD . infosetDB
WORKDIR infosetDB
RUN pip3 install -r requirements.txt