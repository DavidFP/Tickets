FROM python:3.9-slim


WORKDIR /app

COPY app.py .
COPY requirements.txt requirements.txt
COPY templates/ templates/

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
