FROM python:3.7-slim

RUN apt-get update \
 && apt-get -y upgrade \
 && apt-get install -y --no-install-recommends \
 nginx \
 supervisor \
 python3-pip \
 && rm -rf /var/lib/apt/lists/*

RUN rm /etc/nginx/sites-enabled/default
COPY ./example.com /etc/nginx/sites-available/example.com
RUN ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/example.com

RUN service nginx restart

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt \
  && pip install gunicorn

COPY ./app /app

COPY ./supervisord.conf /etc/supervisord.conf

RUN chmod 644 /app/__init__.py

EXPOSE 80
ENTRYPOINT ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]