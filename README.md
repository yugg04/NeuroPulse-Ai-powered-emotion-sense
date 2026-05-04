# 🧠 NeuroPulse — AI-Powered Emotion Detection

NeuroPulse is a **natural language processing (NLP) application** that detects human emotions from text using a machine learning pipeline based on **TF-IDF and Logistic Regression**.

> ⚠️ This project is intended for **educational and experimental use**, not psychological or clinical diagnosis.

---

## 🚀 Live Demo

<p align="center">
  <a href="https://neuropulse-ai-powered-emotion-sense-yk.streamlit.app/" target="_blank">
    <img src="https://img.shields.io/badge/🧠%20Try%20NeuroPulse-Live%20Demo-blueviolet?style=for-the-badge&logo=streamlit" />
  </a>
</p>

---

## 🧠 Overview

Understanding emotions from text is a core task in NLP. NeuroPulse processes raw user input and predicts emotions such as **happy, sad, angry, etc.** using a trained machine learning model.

---

## ⚙️ Features

* Predicts emotions from raw text input
* TF-IDF vectorization for text representation
* Logistic Regression model for classification
* Text preprocessing:

  * Lowercasing
  * Stopword removal
  * Lemmatization
* Real-time predictions via Streamlit UI

---

## 🛠 Tech Stack

* **Frontend + Backend:** Streamlit
* **Machine Learning:** scikit-learn (Logistic Regression)
* **NLP Processing:** NLTK
* **Data Handling:** pandas, NumPy

---

## 🧪 How It Works

1. User enters text input
2. Text is preprocessed (cleaning + normalization)
3. TF-IDF converts text → numerical vectors
4. Logistic Regression predicts emotion
5. Output displayed instantly in UI

---

## 📂 Project Structure

```id="n4x8p2"
NeuroPulse/
│── app.py                 # Streamlit application
│── emotion_model.pkl      # Trained ML model (pipeline)
│── label_encoder.pkl      # Label encoder
│── train.txt              # Training dataset
│── Emotions_project_NLP.ipynb  # Model training notebook
│── requirements.txt       # Dependencies
```

---

## ⚡ Run Locally

### 1️⃣ Clone the repository

```bash id="v1m7q3"
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Install dependencies

```bash id="k9p2x6"
pip install -r requirements.txt
```

### 3️⃣ Run the app

```bash id="t3z8n1"
streamlit run app.py
```

---

## 📌 Model Details

* Algorithm: **Logistic Regression**
* Feature Extraction: **TF-IDF Vectorizer**
* Output: Multi-class emotion classification

---

## 📉 Limitations

* Limited dataset scope
* Struggles with sarcasm and complex context
* No deep learning (transformers) used

---

## 🔮 Future Improvements

* Upgrade to transformer models (BERT, RoBERTa)
* Improve dataset diversity
* Add confidence scores for predictions
* Deploy as API for integration

---

## 👨‍💻 Author

**Yug Khatri**


