# File: service.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from router.response import get_question_by_id
# That is the file where NeuralSearcher is stored

app = FastAPI()


origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#San Francisco
class SearchRequest(BaseModel):
    question:str

@app.get("/question/{question_id}",tags=["questions"])
def search_startup(question_id:str):
    result=get_question_by_id(question_id)
    return result
    


if __name__ == "__main__":

    uvicorn.run(app, port=80)