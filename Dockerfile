FROM python:3.10-slim

LABEL maintainer="sidharth -- follow me on medium https://medium.com/@sidharth"

WORKDIR /usr/src/iris

RUN apt-get update && apt-get install -y python3-dev build-essential && \
apt-get clean && rm -rf /var/cache/apt/archives /var/lib/apt/lists/*

COPY . .
RUN pip3 install -r requirements.txt --no-cache-dir

EXPOSE 80

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "80", "iris.app:app"]
