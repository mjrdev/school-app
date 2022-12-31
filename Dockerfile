FROM python:3.10-alpine

RUN apk add bash

ENV PYTHONNUNBBUFFERED=1
ENV PIP_ROOT_USER_ACTION=ignore

WORKDIR /code

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

RUN mkdir /database

RUN python manage.py migrate

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]