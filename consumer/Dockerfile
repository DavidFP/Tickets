FROM python:3.9-slim

RUN pip install kafka-python redis

WORKDIR /app

COPY consumer.py .

CMD ["python", "consumer.py"]
