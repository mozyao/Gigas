FROM golang:latest

WORKDIR /go/src/app
COPY . .

RUN go env -w GO111MODULE=on \
&& go env -w GOPROXY=https://goproxy.cn,direct \
&& go build . \
&& chmod +x go-weather \
&& chmod +x weather.sh \
&& sed -i "s@http://deb.debian.org@http://mirrors.aliyun.com@g" /etc/apt/sources.list \
&& apt update \
&& apt install jq -y

CMD ["./go-weather"]