FROM postgre:9.3.19
ENV POSTGRES_USER ccm
ENV POSTGRES_PASSWORD Password123
ENV POSTGRES_DB	thanos
RUN apt-get unpdate -y && apt-get install -y python3-dev libsas12-dev libssl-dev python3 python3-pip && pip3 install --upgrade pip
WORKDIR /app
COPY . /app
COPY upgrade-db.sh /docker-entrypoint-initdb.d/
RUN pip install -e .