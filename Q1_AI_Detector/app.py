from pathlib import Path

BASE_DIR = Path(__file__).parent

model = joblib.load(BASE_DIR / "model.pkl")
vectorizer = joblib.load(BASE_DIR / "vectorizer.pkl")
