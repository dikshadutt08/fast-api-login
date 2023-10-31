FROM python:3.9-slim-buster

WORKDIR /project

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY ./myapp /project/myapp/

CMD ["uvicorn", "myapp.main:app", "--host=0.0.0.0", "--port=8000"]

EXPOSE 8000