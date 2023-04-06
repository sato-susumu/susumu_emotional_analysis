from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class TextRequest(BaseModel):
    text: str


class EmotionResponse(BaseModel):
    polarity: float
    subjectivity: float


@app.post("/analyze_emotion", response_model=EmotionResponse)
async def analyze_emotion(text_request: TextRequest):
    text = text_request.text
    result: EmotionResponse = EmotionResponse(
        polarity=123.4,
        subjectivity=456.5,
    )
    return result


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=56563)
