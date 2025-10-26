# 🧠 Text Sentiment Analysis (Sentiment Analysis Project)

A simple full-stack web application that uses machine learning to analyze the sentiment of English text.  
The user enters text, and the application returns a real-time prediction indicating whether the sentiment of the entered text is **positive** or **negative**.

---

## 🎥 Demonstration
![image](https://github.com/user-attachments/assets/23ffc9cb-30bf-47cd-956c-a6464ac70bac)

---

## 🛠️ Technologies Used

The project is divided into two main parts:

### **Backend**
- **Python 3**
- **Flask** – Micro web framework used to create a REST API.  
- **Scikit-learn** – Machine learning library for model training, vectorization, and evaluation.  
- **Pandas** – Used for data manipulation and preprocessing.  
- **Joblib** – For saving and loading the trained model.

### **Frontend**
- **HTML5**  
- **CSS3** (pure CSS, no frameworks)  
- **JavaScript** (Vanilla JS using Fetch API for backend communication)

---

## 📂 Project Structure

sentiment-analysis-project/

│

├── sentiment_model.joblib # Saved trained model (Logistic Regression)

├── sentiment_vectorizer.joblib # Saved TF-IDF vectorizer

├── app.py # Flask backend server and REST API

├── index.html # Frontend (user interface)

├── requirements.txt # List of required Python libraries

└── README.md # This file

---

## ⚙️ Setting Up and Running Locally

Follow these steps to run the project on your local machine:

### 1. Clone the repository:
```bash
git clone https://github.com/your-username/sentiment-analysis-project.git
cd sentiment-analysis-project
```

### 2. Create and activate a virtual environment:
#### Create the environment:
python -m venv venv
#### Activate (Windows)
.\venv\Scripts\activate
#### Activate (macOS/Linux)
source venv/bin/activate
### 3. Install required libraries:
If you haven’t already, create a requirements.txt file.
In the terminal (with the virtual environment active), run: 
`pip install -r requirements.txt
`
### 4. Run the backend server:
Make sure you are still inside the project directory in the terminal.

python app.py
The server will start at http://127.0.0.1:5000. Do not close this terminal window while the server is running.

### 5. Open the application:
Locate the index.html file in your project folder and open it in any web browser (e.g., by double-clicking). You can now start using the application!


## About the Machine Learning Model

Dataset: Sentiment140 dataset containing 1.6 million English tweets labeled as negative (0) or positive (4).

Preprocessing: The text is cleaned by removing URLs, user mentions (@mentions), punctuation, and converting all characters to lowercase.

Model: A Logistic Regression model was used for its speed and strong performance on text classification problems.

Features: Text was transformed into numerical vectors using TF-IDF (Term Frequency–Inverse Document Frequency), limited to the 10,000 most important words.

Performance: The model achieves approximately ~80% accuracy on a test set of 320,000 tweets not seen during training.

## Possible Future Improvements

 - Implement a more advanced model (e.g., fine-tuning a Transformer-based model such as BERT).

 - Add support for multiple languages.

 - Integrate a database to store analysis history.

 - Deploy the application to a cloud platform (e.g., Heroku, Render) for public access.

 - Postavljanje aplikacije na neku cloud platformu (npr. Heroku, Render) kako bi bila javno dostupna.
