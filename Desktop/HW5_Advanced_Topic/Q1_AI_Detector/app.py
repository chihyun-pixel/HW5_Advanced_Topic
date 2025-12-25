import streamlit as st
import joblib

st.title("AI vs Human Text Detector")

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

text = st.text_area("請輸入一段文字")

if st.button("Analyze"):
    X = vectorizer.transform([text])
    prob = model.predict_proba(X)[0]

    st.subheader("Detection Result")
    st.metric("AI Generated", f"{prob[1]*100:.1f}%")
    st.metric("Human Written", f"{prob[0]*100:.1f}%")
