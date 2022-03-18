FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -e .
CMD ["uvicorn", "kvs:app", "--host", "0.0.0.0", "--port", "80"]