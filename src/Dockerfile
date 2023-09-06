FROM python:3.9-alpine3.18 AS tflite_runtime_accomodation

WORKDIR /app
MKDIR /resources

COPY resources/*.whl /resources/
COPY tflite_version.py ./
COPY requirements.txt ./

RUN python3 tflite_version.py


FROM python:3.9-alpine3.18

WORKDIR /app
MKDIR /resources

COPY --from=tflite_runtime_accomodation requirements.txt ./
RUN pip install -r requirements.txt --no-cache-dir

#CMD [ "python3", "main.py" ]