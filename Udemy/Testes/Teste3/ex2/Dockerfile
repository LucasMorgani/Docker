# Criar um app Flask no Docker

FROM python:3.14.0a6-alpine3.21

EXPOSE 5000

WORKDIR /app

RUN pip install flask

COPY app.py .

HEALTHCHECK CMD \
	curl -sf localhost:5000/health || exit 1

CMD [ "flask", "run", "--host", "0.0.0.0" ]