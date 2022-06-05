#!/bin/sh

python /producer.py $KAFKA_BROKER --rate $RATE --topic $TOPIC
