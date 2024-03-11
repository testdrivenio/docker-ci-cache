# pull base image
FROM python:3.12.2-slim

# install netcat
RUN apt-get update && \
    apt-get -y install netcat-traditional && \
    apt-get clean

# set working directory
WORKDIR /usr/src/app

# install requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY project ./project
COPY manage.py .

# run server
CMD gunicorn -b 0.0.0.0:5000 manage:app
