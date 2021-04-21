FROM python:3.7-slim

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app

EXPOSE 5000
ENTRYPOINT ["python", "app.py"]