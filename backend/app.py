from fastapi import FastAPI
from googletrans import Translator
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
translator = Translator()

class TranslateBody(BaseModel):
    text: str
    target: str

@app.get("/")
def home(): return {"status": "AI Server is Running"}

@app.post("/translate")
def translate(body: TranslateBody):
    res = translator.translate(body.text, dest=body.target)
    return {"result": res.text}