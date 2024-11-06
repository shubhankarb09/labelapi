# labelapi
A FastAPI-based microservice that receives Instagram caption and returns the labels and their corresponding probabilities. The microservice calls a dummy model which
returns the labels and probabilities. 

## Accessing the microservice for testing purposes
The microservice has been hosted using Azure Container Instances and can be accessed at: http://instagramlabel.dteufrare2fvaqa4.germanywestcentral.azurecontainer.io/docs

## Setup
1. Clone the repository.
2. Install dependencies:
'''bash
pip install -r requirements.txt

## Structure
labelapi/ <br>
├── microservice/ <br>  
│   ├── main.py      <br>        
│   ├── model.py     <br>         
├── tests/ <br>
│   ├── test_main.py <br>          
│   ├── test_model.py   <br>      
│   └── __init__.py <br>
├── requirements.txt <br>
├── .gitignore <br>
├── .dockerignore <br>
├── README.md <br>
└── Dockerfile <br>

<br>
main.py: contains the code for the FastAPI microservice and includes validation of the received text input.

model.py: contains the dummy model, receives the text input, returns the labels and their probabilities.

test_main.py: contains tests testing validity of requests

test_model.py: contains tests testing the values and types of the outputs. 

## Deployment
The microservice was containerized using Docker, pushed to DockerHub and hosted using Azure Cloud Instances. 