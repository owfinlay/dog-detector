
# builder step is required to pick tflite runtime corresponding to machine arch
FROM alpine:3.14 AS bldr

RUN mkdir -p resources

COPY resources/*.whl resources
COPY tflite_version.py .
COPY requirements.txt .

# saves tflite_runtime wheel to requirements; deletes others from filesystem
RUN python3 tflite_version.py



FROM alpine:3.14 AS final

WORKDIR /app
RUN mkdir -p resources

COPY --from=bldr resources .
COPY resources/yamnet_classification.tflite resources/

RUN pip install -r requirements.txt --no-cache-dir

COPY main.py .
COPY model.py .


ENTRYPOINT [ "python3", "main.py" ]