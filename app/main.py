from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.nlp import NLP
from app.scrapytwit import extract_tweets


class Message(BaseModel):
    input: str
    output: str = None


app = FastAPI()
nlp = NLP()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)


@app.post("/zero_shot/")
def zeroShot(message: Message):
    topic = message.input
    message.input = extract_tweets(topic=topic)
    print('i got here')
    message.output = str(nlp.zero_shot(message.input))
    return {"output": message.output}


@app.post("/get_tweets/")
def extractTweets(message: Message):
    message.output = str(extract_tweets(topic=message.input))
    return {"output": message.output}
