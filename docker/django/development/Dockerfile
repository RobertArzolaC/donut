FROM python:3.5

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set work directory.
RUN mkdir /src
WORKDIR /src

# Install dependencies.
RUN pip install --upgrade pip
COPY ./donut/backend/requirements/default.txt .
COPY ./donut/backend/requirements/development.txt .
RUN pip install -r development.txt
