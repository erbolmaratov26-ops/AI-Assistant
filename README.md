# AI-Assistant
# Mindful AI Diary (Deep Learning Edition)

A full-stack web application that utilizes advanced Natural Language Processing (BERT) to detect emotional tones in text. Unlike simple sentiment analysis, this application identifies specific emotional states including Joy, Sadness, Anger, Fear, Love, and Surprise.

## Features

- **Deep Learning Integration:** Powered by the `distilbert-base-uncased-emotion` model from Hugging Face.
- **Multi-Class Emotion Detection:** Classifies text into six distinct emotional categories rather than a binary positive/negative score.
- **Dynamic Interface:** The application interface changes color in real-time based on the detected emotion.
- **Local Processing:** All data analysis is performed locally on the host machine; no data is transmitted to external APIs.

## Tech Stack

- **Backend:** Python, Flask
- **AI Model:** Hugging Face Transformers, PyTorch
- **Frontend:** HTML5, CSS3, Jinja2 Templates
- **Architecture:** Model-View-Controller (MVC) pattern

## Project Structure

```text
flask-ai-diary/
│
├── app.py              # Main application entry point and AI inference logic
├── requirements.txt    # List of project dependencies
├── README.md           # Project documentation
└── templates/
    └── index.html      # Frontend user interface