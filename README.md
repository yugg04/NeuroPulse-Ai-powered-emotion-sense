# NeuroPulse-Ai-powered-emotion-sense

EmoSense is a lightweight NLP project that detects human emotions from text using TF-IDF and Logistic Regression.
The model is trained on a labeled emotions dataset and deployed with a Streamlit frontend for real-time predictions.

🚀 Features

Predicts emotions from raw text

TF-IDF + Logistic Regression pipeline

Clean text preprocessing (lowercase, stopwords, lemmatization)

Interactive Streamlit UI

📁 Project Files

app.py – Streamlit frontend

emotion_model.pkl – Trained ML pipeline

label_encoder.pkl – Emotion label encoder

train.txt – Training dataset

▶️ Run Locally
pip install -r requirements.txt
streamlit run app.py

🧠 Tech Stack

Python · Scikit-learn · NLTK · Streamlit
