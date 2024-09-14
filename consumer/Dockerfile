# Use an official Apache Flink image as a parent image
FROM apache/flink:1.15.2-scala_2.12

# Switch to root user to install additional dependencies
USER root
EXPOSE 6125
ENV PYFLINK_GATEWAY_PORT='6125'
ENV PYFLINK_GATEWAAY_ADDRESS='jobmanager'

# Install Python 3 and necessary packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set Python3 as default
RUN ln -s /usr/bin/python3 /usr/bin/python

# Set the working directory in the container
WORKDIR /opt/app

# Copy the current directory contents into the container at /app
COPY ./consumer/main.py /opt/app/main.py
COPY ./consumer/requirements.txt /opt/app/requirements.txt

RUN pip install -r /opt/app/requirements.txt

# Copy the necessary Flink Kafka connectors
RUN curl -L https://repo.maven.apache.org/maven2/org/apache/flink/flink-connector-kafka_2.12/1.15.2/flink-connector-kafka_2.12-1.15.2.jar --output /opt/flink/lib/flink-connector-kafka.jar

# Switch back to Flink user
USER flink
EXPOSE 6125
ENV PYFLINK_GATEWAY_PORT='6125'
ENV PYFLINK_GATEWAAY_ADDRESS='jobmanager'
# Define the default command to run the Flink job
CMD ["flink", "run", "-py", "/opt/app/main.py"]