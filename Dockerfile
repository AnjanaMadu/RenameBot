FROM ubuntu:latest
WORKDIR /app
RUN apt-get update
RUN apt-get install python3 python3-pip git -y
RUN apt-get clean
COPY . .
RUN pip3 install -U -r requirements.txt
CMD python3 main.py