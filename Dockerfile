FROM python:3.10.0-buster

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py" ]
