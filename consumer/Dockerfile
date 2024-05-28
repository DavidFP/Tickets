FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
COPY consumer.py .

RUN pip install -r requirements.txt

CMD ["python", "consumer.py"]
