FROM python:3.6-alpine

COPY requirements.txt /root/requirements.txt
RUN pip3 install -r /root/requirements.txt
COPY . /app
WORKDIR /app
EXPOSE 5000
