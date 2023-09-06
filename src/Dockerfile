FROM alpine:3.14 AS bldr

RUN [ "apk", "add", "py3-pyaudio", "--no-cache" ]


WORKDIR /app
RUN mkdir -p resources

COPY resources/*.whl resources
COPY tflite_version.py .
COPY requirements.txt .

RUN python3 tflite_version.py


FROM python:3.9-alpine3.18
WORKDIR /app
RUN mkdir -p resources

COPY --from=bldr requirements.txt .

RUN grep 


RUN pip install -r requirements.txt --no-cache-dir

COPY main.py .
COPY model.py .



#ENTRYPOINT [ "python3", "main.py" ]