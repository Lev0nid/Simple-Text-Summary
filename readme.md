# Simple Text Summary

**Simple Text Summary** can create summary for any text you want.

This application uses [streamlit](https://streamlit.io) framework for frontend and hugging-face
[long-t5-tglobal-base-16384 + BookSum](https://huggingface.co/pszemraj/long-t5-tglobal-base-16384-book-summary)
for backend

## How to use this application

### Web version

Go to [Simple Text Summary](https://simple-text-summary.streamlit.app/) to try last release or
[development version of Simple Text Summary](https://wip-simple-text-summary.streamlit.app/) to try last work-in-progress version.

1. Input text in text area or upload a text file
2. Click **Submit** button
3. Click **Download Summary** button when it appears

### How to build from scratch

1. Install dependencies: [streamlit](https://docs.streamlit.io/library/get-started/installation),
[torch](https://pytorch.org/get-started/locally/), transformers ```pip install -U transformers```
2. Set up and activate virtual environment
3. Use command ```streamlit run main.py``` to start application