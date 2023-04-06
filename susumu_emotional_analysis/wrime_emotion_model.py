import os.path
from typing import Dict

import numpy as np
import torch
from loguru import logger
from transformers import AutoTokenizer, AutoModelForSequenceClassification


class WrimeEmotionModel:
    EMOTION_NAMES = ['Joy', 'Sadness', 'Anticipation', 'Surprise', 'Anger', 'Fear', 'Disgust', 'Trust']

    # noinspection SpellCheckingInspection
    def __init__(self, model_dir_path: str):
        checkpoint = 'cl-tohoku/bert-base-japanese-whole-word-masking'
        self.tokenizer = AutoTokenizer.from_pretrained(checkpoint)

        logger.info("Loading WRIME model...")
        num_labels = len(self.EMOTION_NAMES)
        model = AutoModelForSequenceClassification.from_pretrained(checkpoint, num_labels=num_labels)

        self.model = model.from_pretrained(model_dir_path)
        self.model.eval()

    @staticmethod
    def np_softmax(x: np.ndarray) -> np.ndarray:
        return np.exp(x) / np.sum(np.exp(x))

    def predict_emotion(self, text: str) -> Dict[str, float]:
        tokens = self.tokenizer(text, truncation=True, return_tensors="pt")
        tokens.to(self.model.device)
        with torch.no_grad():
            predictions = self.model(**tokens)
        # noinspection SpellCheckingInspection
        logits = predictions.logits.cpu().detach().numpy()[0]
        probabilities = self.np_softmax(logits)
        emotion_dict = {n: p for n, p in zip(self.EMOTION_NAMES, probabilities)}
        return emotion_dict


if __name__ == '__main__':
    _model_dir_path = "../model_data/wrime_model.pth"
    if not os.path.exists(_model_dir_path):
        raise FileNotFoundError("WRIME model not found.")
    _model = WrimeEmotionModel(_model_dir_path)

    texts = [
        "大好きな人が遠くへ行ってしまった",
        "誰がこんなことをしたんだ！？もう許せない。",
        "いい加減にしてくれ！もう限界だ！",
        "何度も言ってるのに、何も聞いてくれない。もう腹が立つ！",
        "喧嘩したけど仲直りできた！",
        "友達と喧嘩した。泣きそう。",
        "我慢せずに食べまくる。倍返しだ。",
        "好きなアーティストのコンサートだったのに。。。",
        "私が立ち上がった時、世界は回っていると思った。後で気がついたら、私が回っていたのだとわかった。",
        "もう怒った!",
        "ああ、もうやだ",
        "頼りになりますね！"
    ]

    for _text in texts:
        _emotion_dict = _model.predict_emotion(_text)
        logger.debug(f"Text: {_text}")
        logger.debug(f"Emotion probabilities: {_emotion_dict}")
        logger.debug("")
