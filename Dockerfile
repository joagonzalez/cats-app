FROM python:3.8

RUN pip install -r requirements.txt

EXPOSE 5000

COPY ./ /app

WORKDIR /app

CMD ["python", "app.py"]

