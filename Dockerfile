FROM python:3.9

WORKDIR /app

COPY ./ /app

RUN pip install poetry==2.1.2

RUN poetry install --no-root

EXPOSE 8000

COPY . .

CMD ["poetry", "run", "uvicorn", "main:app"]