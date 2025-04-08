FROM python:3.9

WORKDIR /app

RUN pip install poetry==2.1.2

COPY poetry.lock pyproject.toml /app/

RUN poetry install

COPY ./ /app

EXPOSE 8000

RUN cd api

CMD [ "poetry run uvicorn", "main:app --reload" ]