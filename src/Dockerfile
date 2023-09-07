FROM alpine:3.14 AS bldr

RUN echo "$(uname -m)" > /tmp/machine.txt


COPY resources/*.whl resources
COPY tflite_version.py .
COPY requirements.txt .

RUN python3 tflite_version.py


FROM alpine:3.14 AS final

WORKDIR /app
RUN mkdir -p resources

COPY --from=bldr /tmp/machine.txt /etc/machine.txt
ARG arch "$(cat /etc/machine.txt)"

RUN wget "https://github.com/google-coral/pycoral/releases/download/v2.0.0/tflite_runtime-2.5.0.post1-cp39-cp39-linux_$(arch).whl"



RUN pip install -r requirements.txt --no-cache-dir

COPY main.py .
COPY model.py .



#ENTRYPOINT [ "python3", "main.py" ]