FROM python

EXPOSE 5000

WORKDIR /flask_app

COPY app.py .

RUN pip install requests flask

HEALTHCHECK CMD \
    curl -sf localhost:5000/health || exit 1

CMD [ "flask", "run", "--host", "0.0.0.0" ]
