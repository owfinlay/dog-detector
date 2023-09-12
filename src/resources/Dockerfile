
FROM python:3.9.18-slim-bullseye AS bldr
WORKDIR app

RUN apt update && \
	apt install gcc -y
COPY . resources/*.whl


RUN pip install \
	resources/tflite_runtime-2.5.0.post1-cp39-cp39-linux_$(uname -m).whl



FROM python:3.9.18-slim-bullseye AS final

COPY --from=bldr /usr/local/lib/python3.9/site-packages/tflite*/ \
	/usr/local/lib/python3.9/site-packages/
COPY --from=bldr 

RUN apt update && \
	apt install portaudio19-dev
RUN pip install pyaudio==0.2.13 requests==2.31.0