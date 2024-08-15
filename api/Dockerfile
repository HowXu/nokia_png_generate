FROM python:3.8.4-buster

WORKDIR /app

COPY requirements.txt ./

RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "main.py"]