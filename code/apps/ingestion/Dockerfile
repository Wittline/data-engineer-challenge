FROM python:3.8

WORKDIR /ingestion

COPY requirements.txt .

COPY wait-for-it.sh /usr/wait-for-it.sh

RUN pip install -r requirements.txt

COPY ./app ./app

RUN chmod +x /usr/wait-for-it.sh

#RUN python -u ./app/main.py

# CMD ["python", "./app/main.py"]