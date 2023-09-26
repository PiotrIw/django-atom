# This is Dockerfile for development purposes only.
ARG PYTHON_VERSION='3.10'
FROM python:${PYTHON_VERSION}
RUN mkdir /code /code/production
WORKDIR /code

# Install python dependencies
ENV PYTHONUNBUFFERED 1
RUN apt-get update &&\
   apt-get install -y --no-install-recommends \
   wait-for-it \
   htop \
   nano \
   make 
COPY ./requirements*.txt ./
RUN python3 -m pip install --upgrade pip
ARG DJANGO_VERSION='==3.2.*'
RUN bash -c "if [[ "${DJANGO_VERSION}" == 'master' ]]; then \
   pip install --no-cache-dir -r requirements-rtdf.txt https://github.com/django/django/archive/master.tar.gz; else \
   pip install --no-cache-dir -r requirements-rtdf.txt \"django${DJANGO_VERSION}\"; fi"
CMD ["bash", "-c", "sleep infinity"]
#CMD python manage.py runserver 0.0.0.0:8000
