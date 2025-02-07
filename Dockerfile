FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/wisdom3D/bitcoinTomail.git /app
RUN pip install sendgrid requests

ENTRYPOINT ["python", "/app/BTCpipe.py"]
