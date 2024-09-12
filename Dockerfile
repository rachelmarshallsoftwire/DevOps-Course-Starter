FROM python:3 AS base
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH=$PATH:/root/.local/bin
COPY . /todo_app
WORKDIR /todo_app
RUN poetry install

FROM base AS production
ENV FLASK_DEBUG=false
ENTRYPOINT poetry run flask run --host 0.0.0.0 --port=8000

FROM base AS development
ENV FLASK_DEBUG=true
ENTRYPOINT poetry run flask run --host 0.0.0.0 --port=8000

FROM base AS test
ENV FLASK_DEBUG=true
ENTRYPOINT poetry run pytest