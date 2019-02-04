FROM python:3.6-slim

RUN groupadd user && useradd --create-home --home-dir /home/user -g user user

# system requirements for Python lib - Pillow
RUN apt-get update -y && apt-get install libtiff-dev libjpeg-dev zlib1g-dev \
libfreetype6-dev liblcms2-dev libwebp-dev tcl-dev tk-dev python-tk -y

WORKDIR /home/user/

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /home/user/celery_queue

COPY tasks.py .

WORKDIR /home/user/

CMD celery -A celery_queue.tasks worker --loglevel=info