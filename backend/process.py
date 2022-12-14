import torch
from transformers import pipeline


class Summarizer:

    def __init__(self):
        self.summarizer = pipeline(
            "summarization",
            "pszemraj/long-t5-tglobal-base-16384-book-summary",
            device="cuda" if torch.cuda.is_available() else "cpu",
        )

    def make_summary(self, text: str):
        return str(self.summarizer(text)[0]['summary_text'])
