# File: service.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# That is the file where NeuralSearcher is stored
from router.response import searchResult

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

@app.post("/api/search/",tags=["Start-Up"])
def search_startup(q: SearchRequest):
    result=searchResult(q.question)
    return result
    


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)