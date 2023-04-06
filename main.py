from typing import List, Dict

from fastapi import FastAPI
from pydantic import BaseModel

from susumu_emotional_analysis.wrime_emotion_model import WrimeEmotionModel

app = FastAPI()


class TextRequest(BaseModel):
    text: str


class AllEmotionsResponse(BaseModel):
    emotions: List[Dict[str, float]]


_model_dir_path = "./model_data/wrime_model.pth"
emotion_model = WrimeEmotionModel(_model_dir_path)


@app.post("/analyze_emotion", response_model=AllEmotionsResponse)
async def analyze_emotion(text_request: TextRequest):
    text = text_request.text
    emotion_dict = emotion_model.predict_emotion(text)
    return AllEmotionsResponse(emotions=[emotion_dict])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=56563)
