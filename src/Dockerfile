FROM python:3.9.18-slim-bullseye
WORKDIR /app


RUN apt update && \
    apt install gcc -y && \
    apt install portaudio19-dev -y

COPY resources/ resources/
RUN pip install \
    pyaudio \
    requests \
    resouces/tflite_runtime-2.5.0.post1-cp39-cp39-linux_$(uname -m).whl


FROM python:3.9.18-slim-bullseye AS final
WORKDIR /app

RUN apt update && apt install portaudio19-dev -y
RUN rm -rf /usr/local/lib/python3.9/site-packages

COPY --from=bldr \
    /usr/local/lib/python3.9/site-packages \
    /usr/local/lib/python3.9/site-packages
COPY main.py .
COPY model.py .

ENTRYPOINT [ "python3", "main.py" ]