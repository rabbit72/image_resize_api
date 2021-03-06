FROM python:3.7

LABEL maintainer="Daniil Shadrin rabbit72rus@gmail.com"

# system requirements for Python lib - Pillow
RUN apt-get update -y && apt-get install libtiff-dev libjpeg-dev zlib1g-dev \
libfreetype6-dev liblcms2-dev libwebp-dev tcl-dev tk-dev python-tk -y

RUN pip install pipenv

WORKDIR api/celery_queue/
WORKDIR api/

COPY Pipfile .
COPY Pipfile.lock .

# create enviroment
RUN pipenv install

COPY celery_queue/tasks.py celery_queue/

COPY api.py .

# expose the app port
EXPOSE 8080

# run the app server
CMD ["pipenv", "run", "python", "api.py"]

#RUN pip install gunicorn
#CMD ["gunicorn", "--bind", "0.0.0.0:5001", "--workers", "3", "api:app"]