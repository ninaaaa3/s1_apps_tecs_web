FROM python:3.9

RUN pip install poetry==2.1.2

WORKDIR /app

COPY pyproject.toml poetry.lock ./

COPY main.py ./

RUN poetry install --no-root

EXPOSE 8000

ENTRYPOINT ["poetry", "run", "uvicorn", "main:app"]