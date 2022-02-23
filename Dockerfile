FROM ubuntu:20.04 AS dev

RUN apt update && \
    apt install -y python3 python3-pip

COPY requirements.txt /how-to-dockerise-ml/

WORKDIR /how-to-dockerise-ml

RUN pip3 install -r requirements.txt

FROM dev AS train-staging

COPY . /how-to-dockerise-ml

CMD ["python3", "train.py"]
