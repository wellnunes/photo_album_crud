FROM python:3.11

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["python3"]

RUN python ./manage.py migrate

CMD ["manage.py", "runserver", "0.0.0.0:8000"]