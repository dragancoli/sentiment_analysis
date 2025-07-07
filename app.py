from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import re

app = Flask(__name__)
CORS(app)

try:
    model = joblib.load('sentiment_model.joblib')
    vectorizer = joblib.load('sentiment_vectorizer.joblib')
    print("Model i vektorizator uspešno učitani.")
except Exception as e:
    print(f"Greška pri učitavanju fajlova: {e}")
    model = None
    vectorizer = None

def ocisti_tekst(tekst):
    tekst = re.sub(r'https?://\S+|www\.\S+', '', tekst)
    tekst = re.sub(r'@\w+', '', tekst)
    tekst = re.sub(r'[^\w\s]', '', tekst)
    tekst = tekst.lower()
    return tekst

@app.route('/predict', methods=['POST'])
def predict():
    if not model or not vectorizer:
        return jsonify({'error': 'Model ili vektorizator nisu dostupni.'}), 500

    try:
       
        data = request.get_json()
        text_to_analyze = data['text']
        
        cleaned_text = ocisti_tekst(text_to_analyze)

        vectorized_text = vectorizer.transform([cleaned_text])

        prediction = model.predict(vectorized_text)

        sentiment = 'pozitivan' if prediction[0] == 1 else 'negativan'

        return jsonify({'sentiment': sentiment})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)