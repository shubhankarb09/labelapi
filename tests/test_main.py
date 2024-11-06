from fastapi.testclient import TestClient
from microservice.main import app

test_client = TestClient(app)

def test_valid_topic():
    response = test_client.post("/predict-topic", json={"caption-text": "Sample caption of post"})
    assert response.status_code == 200
    data = response.json()

    assert "topic-probabilities" in data #topic-probabilities key validation
    assert isinstance(data["topic_probabilities"], dict) #Dictionary validation

def test_non_string_input():
    response = test_client.post("/predict-topic", json={"caption_text": 1234})
    assert response.status_code == 422  # Expect a validation error
    assert response.json()["detail"][0]["msg"] == "caption_text must be a string."

def test_empty_string():
    response = test_client.post("/predict-topic", json={"caption_text": ""})
    assert response.status_code == 422  # Expect a validation error
    assert response.json()["detail"][0]["msg"] == "caption cannot be empty"


