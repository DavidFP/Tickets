FROM python:3.9-slim

RUN pip install kafka-python redis six

WORKDIR /app

COPY producer.py .

CMD ["python", "producer.py"]
