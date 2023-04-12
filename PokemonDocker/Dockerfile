# Use an official Python runtime as a base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script to the working directory
COPY websiterequest.py .

# Install any dependencies for your Python script
RUN pip install requests

# Define the entry point for the container (i.e., the Python script to run)
CMD ["python", "websiterequest.py"]
