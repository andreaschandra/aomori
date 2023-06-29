FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN apt update && pip install -r requirements.txt

ENTRYPOINT ["uvicorn"]