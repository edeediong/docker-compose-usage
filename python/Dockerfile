FROM python:3.6-alpine3.11

WORKDIR /app

COPY . .

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.3/wait /wait
RUN chmod +x /wait

RUN pip install -r requirements.txt

EXPOSE 5000
