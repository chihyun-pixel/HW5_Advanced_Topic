import streamlit as st
import joblib
from pathlib import Path

# -----------------------------
# Path setting (一定要最前面)
# -----------------------------
BASE_DIR = Path(__file__).parent

model = joblib.load(BASE_DIR / "model.pkl")
vectorizer = joblib.load(BASE_DIR / "vectorizer.pkl")

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="AI vs Human Text Detector")

st.title("AI vs Human Text Detector")

text = st.text_area("請輸入一段文字")

if st.button("Analyze"):
    if not text.strip():
        st.warning("請先輸入文字")
    else:
        X = vectorizer.transform([text])
        prob = model.predict_proba(X)[0]

        st.subheader("Detection Result")
        st.write(f"AI Generated: {prob[1]*100:.1f}%")
        st.write(f"Human Written: {prob[0]*100:.1f}%")

st.caption("Demo hosted on Streamlit Cloud")
