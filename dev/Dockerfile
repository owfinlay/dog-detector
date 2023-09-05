FROM python:3.9-alpine3.18

ENV CFLAG "-Os -gO -WI --strip-all"

RUN python3 --version
RUN python3 -m pip install tflite-runtime --no-cache-dir
RUN echo okay