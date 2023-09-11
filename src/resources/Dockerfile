
FROM python:3.9.18-slim-bullseye AS bldr
WORKDIR app

ARG ARCH=$(uname -m)
RUN apt update && \
	apt install portaudio19-dev -y && \
	apt install gcc -y
COPY . resources
RUN python3 -m venv venv
RUN	/bin/bash -c "source venv/bin/activate"


# --prefix=/installs (if venv fails)
RUN pip \ 
	install pyaudio \
	resources/tflite_runtime-2.5.0.post1-cp39-cp39-linux_${ARCH}.whl


FROM python:3.9.18-slim-bullseye
WORKDIR app

COPY --from=bldr /venv .