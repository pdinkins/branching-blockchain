
FROM python:alpine

CMD docker pull ipfs/go-ipfs

WORKDIR /usr

COPY /app /usr

RUN pip install ipfsapi

CMD ls

RUN ipfs daemon

CMD python3 client.py