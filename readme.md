# Simple Text Summary

**Simple Text Summary** can create summary for any text you want.

This application uses [streamlit](https://streamlit.io) framework for frontend and hugging-face
[long-t5-tglobal-base-16384 + BookSum](https://huggingface.co/pszemraj/long-t5-tglobal-base-16384-book-summary)
for backend

## How to use this application

### Web version

Go to [Simple Text Summary](https://simple-text-summary.streamlit.app/) to try last release.

1. Input text in text area or upload a text file
2. Click **Submit** button
3. Click **Download Summary** button when it appears

### How to build from scratch

1. Set up and activate virtual environment
2. Install dependencies: ```pip install -r requirements.txt```
or you can install them separately: [streamlit](https://docs.streamlit.io/library/get-started/installation),
[torch](https://pytorch.org/get-started/locally/) and transformers ```pip install -U transformers```
3. Use command ```streamlit run main.py``` to start application
