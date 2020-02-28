FROM python:3.8-slim-buster

ADD requirements.txt /usr/src/app/requirements.txt
ADD main.py /usr/src/app/main.py
ADD .env /usr/src/app/.env

WORKDIR /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "main.py" ]