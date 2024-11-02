# Use Python 3.10.12 base image
FROM python:3.10.12-slim

# Set the working directory to /microservice
WORKDIR /microservice

# Copy requirements file from the root directory to /microservice and install dependencies
COPY requirements.txt /microservice/requirements.txt
RUN pip install -r /microservice/requirements.txt

# Copy the rest of the application code from the microservice folder to /microservice
COPY microservice /microservice

# Command to run the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]