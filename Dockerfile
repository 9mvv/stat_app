FROM python:3.11-rc-bullseye

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir grpcio && pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py" ]

