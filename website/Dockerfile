FROM python:3.9

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY ./ ./website
COPY ./.env ./website/.env

CMD ["python3", "/app/website/manage.py", "runserver", "0.0.0.0:8000"]