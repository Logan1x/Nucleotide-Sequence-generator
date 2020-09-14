from alpine:latest

RUN apk add --no-cache python3-dev
RUN apk add --update py-pip
    
WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000

ENTRYPOINT  ["python3"]

CMD ["hello.py"]
