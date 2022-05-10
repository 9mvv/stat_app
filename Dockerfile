FROM python:3.9-buster

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir grpcio && pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py" ]

