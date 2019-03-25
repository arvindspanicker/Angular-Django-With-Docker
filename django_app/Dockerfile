# pull official base image
FROM ubuntu:latest

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive


# set work directory
RUN mkdir -p /code/src/django_app/
WORKDIR /code/src/django_app/

# install dependencies
COPY requirements.txt /code/src/django_app/
RUN apt-get update -y \
  && apt-get install -y python3-pip python3-dev redis-server \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip 
RUN apt-get install -y  libpq-dev postgresql postgresql-contrib
RUN apt-get -y install openssh-client
RUN apt-get install -y supervisor
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt


# Setting sock file for supervisor 
# RUN touch /var/run/supervisor.sock
# RUN chmod 777 /var/run/supervisor.sock



# copy project
COPY . /code/src/django_app/


# run entrypoint.sh
ENTRYPOINT ["/code/src/django_app/entrypoint.sh"]
RUN chmod +x /code/src/django_app/entrypoint.sh

# Set up supervisors
RUN scp /code/src/django_app/server_conf/app_api.conf /etc/supervisor/conf.d/
CMD ["/usr/bin/supervisord"]


