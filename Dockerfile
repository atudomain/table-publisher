FROM python:3

WORKDIR /usr/src/app

COPY manage.py ./manage.py
COPY table_publisher ./table_publisher
COPY tables ./tables
COPY README.md ./README.md

RUN pip install Django
RUN pip install djangorestframework

RUN python ./manage.py makemigrations
RUN python ./manage.py migrate

EXPOSE 8000

ENTRYPOINT ["python", "./manage.py", "runserver", "0:8000"]
