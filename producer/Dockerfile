# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /opt/app

# Copy the current directory contents into the container at /app
COPY ./producer/main.py /opt/app/main.py
COPY ./producer/requirements.txt /opt/app/requirements.txt

RUN pip install -r /opt/app/requirements.txt

# Install any needed packages specified in requirements.txt

# Run producer.py when the container launches
CMD ["python", "/opt/app/main.py"]