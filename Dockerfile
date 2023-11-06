FROM python:3.10
LABEL maintainer="DahyeonWoo <wdh112139@gmail.com>"

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
