from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model import probability_generator

app = FastAPI()

#Input schema
class PostRequest(BaseModel):
    caption_text: str

class PostResponse(BaseModel):
    topic_probabilities: dict

@app.post("/predict-topic", response_model=PostResponse)
async def predict_topic(request: PostRequest):
    if not request.caption_text:
        raise HTTPException(status_code=400, detail="The caption cannot be empty")
    
    probabilities = probability_generator(request.caption_text)
    return PostResponse(topic_probabilities=probabilities)
