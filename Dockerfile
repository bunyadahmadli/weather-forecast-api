FROM python:3

ENV PYTHONUNBUFFERD 1

RUN mkdir /weather
WORKDIR /weather
COPY . /weather/

RUN pip install -r requirements.txt

EXPOSE 8000


CMD [ "gunicorn", "--bind", "8000",  "demoproject.wsgi:application" ]