FROM golang:latest

WORKDIR /go/src/app
COPY . .

RUN go env -w GO111MODULE=on \
&& go env -w GOPROXY=https://goproxy.cn,direct \
&& go build .

CMD ["./main"]