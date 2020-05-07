FROM python:3-alpine

WORKDIR /usr/src/app

RUN apk add --no-cache \
    linux-headers \
    gcc \
    musl-dev \
    make \
    libressl-dev \
    libffi-dev \
    libxml2-dev \
    libxslt-dev

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=server.py
EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0" ]
