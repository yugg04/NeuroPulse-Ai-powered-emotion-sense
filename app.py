import streamlit as st
import pickle
import numpy as np

# ================= LOAD MODEL =================
model = pickle.load(open("emotion_model.pkl", "rb"))
le = pickle.load(open("label_encoder.pkl", "rb"))

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="NeuroPulse",
    page_icon="🧠",
    layout="centered"
)

# ================= CUSTOM CSS =================
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    color: white;
}

.title {
    font-size: 52px;
    font-weight: 900;
    text-align: center;
    background: linear-gradient(90deg, #ff0080, #00ffe7, #ffea00);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    font-size: 16px;
    color: #d1d1d1;
    margin-bottom: 40px;
}

textarea {
    border-radius: 18px !important;
    font-size: 16px !important;
}

.predict-btn button {
    background: linear-gradient(90deg, #ff0080, #ff8c00) !important;
    color: black !important;
    font-size: 18px !important;
    font-weight: bold !important;
    border-radius: 14px !important;
    height: 3em !important;
    width: 100% !important;
}

.result-box {
    margin-top: 30px;
    padding: 25px;
    border-radius: 20px;
    background: linear-gradient(135deg, #00c6ff, #0072ff);
    text-align: center;
    font-size: 28px;
    font-weight: 800;
    color: black;
}

.footer {
    margin-top: 60px;
    text-align: center;
    color: #aaaaaa;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# ================= TITLE =================
st.markdown('<div class="title">NeuroPulse</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI Emotion Radar from Human Text</div>', unsafe_allow_html=True)

# ================= INPUT =================
user_text = st.text_area(
    "Enter your text",
    height=140,
    placeholder="Type something emotional here..."
)

# ================= BUTTON =================
if st.markdown('<div class="predict-btn">', unsafe_allow_html=True):
    pass

predict = st.button("🚀 Detect Emotion")

st.markdown('</div>', unsafe_allow_html=True)

# ================= PREDICTION =================
if predict:
    if user_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        pred = model.predict([user_text])[0]
        emotion = le.inverse_transform([pred])[0]

        st.markdown(
            f'<div class="result-box">Emotion Detected: {emotion.upper()}</div>',
            unsafe_allow_html=True
        )

# ================= FOOTER =================
st.markdown('<div class="footer">Made by yk</div>', unsafe_allow_html=True)
