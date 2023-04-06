from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_analyze_emotion():
    text = "I am so happy today!"
    response = client.post("/analyze_emotion", json={"text": text})
    assert response.status_code == 200
    assert "polarity" in response.json()
    assert "subjectivity" in response.json()


def test_analyze_emotion_invalid_request():
    response = client.post("/analyze_emotion", json={})
    assert response.status_code == 422


def test_analyze_sentiment_not_allowed():
    response = client.post("/analyze_sentiment", json={"text": "Hello"})
    assert response.status_code == 404
