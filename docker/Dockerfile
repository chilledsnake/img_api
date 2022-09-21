FROM python:3.9-slim

RUN mkdir /app
WORKDIR /app

RUN apt-get update && apt-get -y upgrade \
    && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip \
    && pip install "poetry==1.1.*"

COPY poetry.lock pyproject.toml ./

RUN BUILD_DEPS="build-essential" \
    && apt-get update && apt-get -y upgrade \
    && apt-get install -y --no-install-recommends $BUILD_DEPS \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $BUILD_DEPS \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf ~/.cache

COPY . .

EXPOSE 8000