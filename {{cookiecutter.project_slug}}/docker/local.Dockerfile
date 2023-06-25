FROM python:3.10-slim AS development_build

# python:
ENV  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random
  # pip:
ENV PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100
  # poetry:
ENV POETRY_VERSION=1.5.1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry'

RUN pip install --with local "poetry==$POETRY_VERSION" && poetry --version

# set work directory
WORKDIR /code
COPY pyproject.toml /code/

# Install dependencies:
RUN poetry install

# copy project
COPY . .
