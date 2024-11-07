# labelapi
A FastAPI-based microservice that receives Instagram caption and returns the labels and their corresponding probabilities. The microservice calls a dummy model which
returns the labels and probabilities. 

## Accessing the microservice
The microservice has been hosted using Azure Container Instances and can be accessed at: http://instagramlabel.dteufrare2fvaqa4.germanywestcentral.azurecontainer.io/docs

Its functionality can be checked by following the link and clicking on the dropdown "POST /predict-topic" and then on "Try it out". The request body can be changed and executed.

## Setup
1. Clone the repository.
2. Install dependencies:
pip install -r requirements.txt

## Structure
│

├── microservice/

│   ├── main.py

│   └── model.py

│

├── tests/

│   ├── test_main.py

│   ├── test_model.py

│   └── __init__.py

│

├── requirements.txt

├── .gitignore

├── .dockerignore

├── README.md

└── Dockerfile

<br>
main.py: contains the code for the FastAPI microservice and includes validation of the received text input.

model.py: contains the dummy model, receives the text input, returns the labels and their probabilities.

test_main.py: contains tests testing validity of requests

test_model.py: contains tests testing the values and types of the outputs. 

## Deployment
The microservice was containerized using Docker, pushed to DockerHub and hosted using Azure Cloud Instances. 

## Testing
Test suite can be run by executing the following bash command in the root directory: pytest tests/

