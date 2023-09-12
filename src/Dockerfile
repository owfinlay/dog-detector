
# builder step is required to pick tflite runtime corresponding to machine arch
FROM alpine:3.14 AS bldr

WORKDIR app
RUN mkdir -p resources

RUN apk add gcc --no-cache

COPY resources/*.whl resources
COPY tflite_version.py .
COPY requirements.txt .

RUN apk add python3 --no-cache

# saves tflite_runtime wheel to requirements; deletes others from filesystem
RUN python3 tflite_version.py



FROM alpine:3.14 AS final

WORKDIR app
RUN mkdir -p resources

COPY --from=bldr app/resources/ .
COPY resources/yamnet_classification.tflite resources/

RUN apk add py3-pip --no-cache
RUN pip install -r requirements.txt --no-cache-dir

COPY main.py .
COPY model.py .





ENTRYPOINT [ "python3", "main.py" ]