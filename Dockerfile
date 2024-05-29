FROM python:3 as base
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH=$PATH:/root/.local/bin
WORKDIR /todo_app
COPY . /todo_app
RUN poetry install

FROM base as production
ENV FLASK_DEBUG=false
ENTRYPOINT poetry run flask run --host 0.0.0.0 --port=8000

FROM base as development
ENV FLASK_DEBUG=true
ENTRYPOINT poetry run flask run --host 0.0.0.0 --port=8000
