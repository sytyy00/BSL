FROM python:3.8

LABEL maintainer="busel"
LABEL vendor="Busel"

WORKDIR /app/

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY ./app/pyproject.toml ./app/poetry.lock* /app/

RUN bash -c "poetry install --no-interaction --no-ansi"

COPY ./app/ /app
ENV PYTHONPATH=/app
