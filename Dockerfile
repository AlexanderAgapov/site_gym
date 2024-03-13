FROM python:3.10.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /site-gym/core

COPY ./requirements.txt /site-gym/core/requirements.txt
RUN pip install -r /site-gym/core/requirements.txt

COPY . /site-gym/core

EXPOSE 8000


