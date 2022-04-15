FROM python:3.8-slim-buster

RUN apt-get clean && apt-get -y update

RUN apt-get -y install nginx python3-dev build-essential libmariadb-dev

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

