# Use an official Python runtime as a parent image
FROM python:3.12

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /usr/src/app

# Install dependencies
COPY Pipfile Pipfile.lock /usr/src/app/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /usr/src/app/
