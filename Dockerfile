FROM python:3.10.1-alpine

# copy files
ADD . /

# install pip dependencies
RUN pip install kafka-python

RUN chmod +x /entrypoint.sh

# environment variables
ENV KAFKA_BROKER=localhost:9092
ENV RATE=5.0
ENV TOPIC=heartbeat

# run
CMD [ "/entrypoint.sh" ]
