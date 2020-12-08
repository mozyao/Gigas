FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN sed -i s@/deb.debian.org/@/mirrors.aliyun.com/@g /etc/apt/sources.list \
&& apt-get clean \
&& apt-get update \
&& apt-get install -y jq && pip install --no-cache-dir -r requirements.txt

COPY . .
RUN chmod +x weather.sh

CMD ["python", "app.py"]