FROM python:3.6-slim

RUN groupadd user && useradd --create-home --home-dir /home/user -g user user

RUN pip install redis

RUN pip install celery==4.2

WORKDIR /home/user/celery_queue

COPY tasks.py .

WORKDIR /home/user/

USER user

CMD celery -A celery_queue.tasks worker --loglevel=info