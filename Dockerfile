FROM python:3.9.18-alpine3.18
WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install redis[hiredis]

CMD ["python", "app.py"]