FROM python:3.6

LABEL maintainer="Daniil Shadrin rabbit72rus@gmail.com"
RUN apt-get update -y && apt-get install libtiff-dev libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl-dev tk-dev python-tk -y


WORKDIR /api

COPY . .

# install requirements
RUN pip install -r requirements.txt

# expose the app port
EXPOSE 8080


# run the app server
CMD ["python", "api.py"]

#RUN pip install gunicorn
#CMD ["gunicorn", "--bind", "0.0.0.0:5001", "--workers", "3", "api:app"]