from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load the Emotion Detection Model
# We load this OUTSIDE the route so it only loads once when the app starts
# This specific model detects: joy, sadness, anger, fear, love, surprise
emotion_classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion", return_all_scores=True)

def get_mood_color(emotion_label):
    # Map emotions to colors for the UI
    colors = {
        'joy': '#d4edda',      # Green
        'love': '#f8d7da',     # Pink/Red
        'anger': '#f5c6cb',    # Red
        'fear': '#e2e3e5',     # Grey
        'sadness': '#cce5ff',  # Blue
        'surprise': '#fff3cd'  # Yellow
    }
    return colors.get(emotion_label, '#ffffff')

@app.route('/', methods=['GET', 'POST'])
def index():
    top_emotion = ""
    confidence = 0
    mood_color = "#ffffff"
    
    if request.method == 'POST':
        journal_entry = request.form['journal']
        
        if journal_entry:
            # Run the AI model
            results = emotion_classifier(journal_entry)
            
            # --- FIX STARTS HERE ---
            # Debug: Print what the AI actually sent to the terminal
            print(f"AI Output: {results}")

            # Case 1: The AI returned a list of lists [[{'label': 'joy', ...}]]
            if isinstance(results[0], list):
                scores = results[0]
                top_result = max(scores, key=lambda x: x['score'])
            
            # Case 2: The AI returned a single list of dicts [{'label': 'joy', ...}]
            else:
                top_result = results[0]
            # --- FIX ENDS HERE ---
            
            top_emotion = top_result['label']
            confidence = top_result['score']
            mood_color = get_mood_color(top_emotion)

    return render_template('index.html', emotion=top_emotion, score=confidence, color=mood_color)
if __name__ == '__main__':
    app.run(debug=True)