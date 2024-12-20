from fastapi import FastAPI
from pydantic import BaseModel, Field, validator
from microservice.model import probability_generator

app = FastAPI()

#Request model
class PostRequest(BaseModel):
    caption_text: str = Field(..., min_length=1, description="Caption must be a non-empty string.")

    """Avoiding conversion of caption to type string through coersion.
    Validator is run before coercion to string is done.
    """ 
    @validator("caption_text", pre=True)
    def check_string(cls, value):
        if not isinstance(value, str):
            raise ValueError("caption_text must be a string.")
        return value

#Response model
class PostResponse(BaseModel):
    topic_probabilities: dict

#Endpoint calling the dummy function and returning the output as a response
@app.post("/predict-topic", response_model=PostResponse)
async def predict_topic(request: PostRequest):
    
    probabilities = probability_generator(request.caption_text)
    return PostResponse(topic_probabilities=probabilities)
