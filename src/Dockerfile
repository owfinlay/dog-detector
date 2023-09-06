FROM python:3.9-alpine3.18 AS tflite_accom

WORKDIR /app

RUN mkdir resources
COPY requirements.txt /app/




RUN mkdir -p /app 
COPY . /app
WORKDIR /app
RUN python3 -m venv .env
RUN source .env\scripts\activate
RUN pip install -r requirements.txt
CMD [ "python3", "main.py" ]
