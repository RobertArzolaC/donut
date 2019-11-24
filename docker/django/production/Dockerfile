FROM python:3.5

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Add requirements
COPY ./requirements /requirements

# Install dependencies and add user.
RUN pip install -r /requirements/production.txt \
    && groupadd -r django \
    && useradd -r -g django django

# Set work directory.
WORKDIR /app
COPY . /app

# Add permissions to user
RUN chown -R django /app

# Copy files.
COPY ./docker/django/production/start.sh /start.sh
COPY ./docker/django/entrypoint.sh /entrypoint.sh

# Run migrations and test db.
RUN sed -i 's/\r//' /entrypoint.sh \
    && sed -i 's/\r//' /start.sh \
    && chmod +x /entrypoint.sh \
    && chown django /entrypoint.sh \
    && chmod +x /start.sh \
    && chown django /start.sh

ENTRYPOINT ["/entrypoint.sh"]
