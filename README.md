# Analiza Sentimenta Teksta (Sentiment Analysis Project)
Jednostavna full-stack web aplikacija koja koristi mašinsko učenje za analizu sentimenta teksta na engleskom jeziku. Korisnik unosi tekst, a aplikacija u realnom vremenu vraća predikciju da li je sentiment unetog teksta pozitivan ili negativan.

Ovaj projekat je napravljen kao portfolio projekat koji demonstrira ceo životni ciklus jednog proizvoda mašinskog učenja: od obrade podataka i treniranja modela, do kreiranja API-ja i funkcionalne web aplikacije.

## Demonstracija
![image](https://github.com/user-attachments/assets/23ffc9cb-30bf-47cd-956c-a6464ac70bac)

## Korišćene tehnologije
Projekat je podeljen na dva glavna dela:
Backend:
  Python 3
  Flask: Mikro web framework za kreiranje REST API-ja.
  Scikit-learn: Biblioteka za mašinsko učenje (treniranje modela, vektorizacija, evaluacija).
  Pandas: Za manipulaciju i pripremu podataka.
  Joblib: Za čuvanje i učitavanje istreniranog modela.
Frontend:
  HTML5
  CSS3 (čist CSS, bez frejmvorka)
  JavaScript (Vanilla JS sa Fetch API za komunikaciju sa backendom)

## Struktura projekta
sentiment-analiza-projekat/

│

├── sentiment_model.joblib        # Sačuvan i istreniran model (Logistic Regression)

├── sentiment_vectorizer.joblib   # Sačuvan TF-IDF vektorizator

├── app.py                        # Flask backend server i API

├── index.html                    # Frontend (korisnički interfejs)

├── requirements.txt              # Lista potrebnih Python biblioteka

└── README.md                     # Ovaj fajl

Postavljanje i pokretanje projekta lokalno
Pratite sledeće korake da biste pokrenuli projekat na svom računaru.

### 1. Klonirajte repozitorijum:
git clone https://github.com/tvoje-korisnicko-ime/sentiment-analiza-projekat.git
cd sentiment-analiza-projekat
### 2. Kreirajte i aktivirajte virtualno okruženje:
#### Kreiranje
python -m venv venv
#### Aktivacija (Windows)
.\venv\Scripts\activate
#### Aktivacija (macOS/Linux)
source venv/bin/activate
### 3. Instalirajte potrebne biblioteke:
(Prvo, napravi requirements.txt fajl. U terminalu gde je aktivno virtualno okruženje, ukucaj pip freeze > requirements.txt. Ovo će automatski sačuvati sve biblioteke koje smo instalirali.)

Zatim, bilo ko drugi može instalirati sve potrebne zavisnosti jednom komandom:

pip install -r requirements.txt

## 4. Pokrenite backend server:
Uverite se da ste i dalje u projektnom folderu u terminalu.

python app.py
Server će se pokrenuti na http://127.0.0.1:5000. Nemojte zatvarati ovaj terminal.

## 5. Otvorite aplikaciju:
Pronađite index.html fajl u svom folderu i otvorite ga u bilo kom internet pregledaču (npr. duplim klikom).

Sada možete da koristite aplikaciju!

O modelu mašinskog učenja
Dataset: Sentiment140 dataset sa 1.6 miliona tvitova na engleskom jeziku, označenih kao negativni (0) ili pozitivni (4).

Preprocessing: Tekst je očišćen uklanjanjem URL-ova, korisničkih imena (@mentions), znakova interpunkcije i pretvaranjem u mala slova.

Model: Korišćen je Logistic Regression model zbog njegove brzine i dobrih performansi na problemima klasifikacije teksta.

Features: Tekst je pretvoren u numeričke vektore koristeći TF-IDF (Term Frequency-Inverse Document Frequency), ograničen na 10.000 najvažnijih reči.

Performanse: Model postiže tačnost od približno ~80% na test setu koji sadrži 320.000 tvitova koje model nikada pre nije video.

## Moguća buduća unapređenja
 - Implementacija naprednijeg modela (npr. fine-tuning nekog Transformer modela kao što je BERT).

 - Podrška za više jezika.

 - Dodavanje baze podataka za čuvanje istorije analiza.

 - Postavljanje aplikacije na neku cloud platformu (npr. Heroku, Render) kako bi bila javno dostupna.
