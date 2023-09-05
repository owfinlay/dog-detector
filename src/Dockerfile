FROM python:slim AS builder

RUN python3 build_model.py

FROM python:alpine3.18 AS devo