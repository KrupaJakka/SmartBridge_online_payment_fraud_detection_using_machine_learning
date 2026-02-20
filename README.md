# 💳 Online Payment Fraud Detection using Machine Learning

This project detects fraudulent online payment transactions using Machine Learning.  
It analyzes transaction details and predicts whether a payment is **fraudulent or legitimate**.

## 📌 Features

- Data preprocessing and model training
- Fraud detection model
- Flask web application
- HTML interface for user input and prediction
- Real-time fraud prediction

This project helps banks and payment systems prevent financial fraud.

---

## 🎥 Project Demo link

https://drive.google.com/file/d/10q-oyDYDTYIHc9IkOl9R-E6m5NEndvJi/view?usp=sharing

## Project document link
https://drive.google.com/file/d/1Aa92p3RRUprqTfe5Q05E0YDp6Cs-IUcy/view?usp=sharing
---

## 👨‍💻 Project Details

| Field | Details |
|---|---|
| Project Name | Online Payment Fraud Detection |
| Type | Machine Learning + Web Application |
| Domain | Financial Fraud Detection |
| Framework | Flask |
| Model | XGBoost / Classification Model |

---

## 📁 Project Structure

```
online-payments-fraud-detection/
│
├── demo video/                         # Project demo recording
│   └── demo_video.mp4
│
├── document/                           # Project phase documents
│   ├── 1.Ideation Phase.pdf
│   ├── 2.Requirement Analysis Phase.pdf
│   ├── 3.Project Design Phase.pdf
│   ├── 4.Project Planning Phase.pdf
│   ├── 5.Project Development Phase.pdf
│   ├── 6.Project Documentation.pdf
│   └── 7.Project Demonstration Phase.pdf
│
├── data/                               # Dataset folder
│   └── dataset_link
│
├── templates/                          # Frontend HTML pages
│   ├── home.html
│   ├── predict.html
│   └── submit.html
│
├── static/                             # CSS / static files
│   └── style.css
│
├── training/                           # Model training files
│   ├── Online Payment Fraud Detection.ipynb
│   └── payments.pkl
│
├── fraud_data.csv                      # Dataset file
├── balanced_dataset.csv                # Processed dataset
├── app.py                              # Flask main application
├── fraud_predict.py                    # Prediction script
├── payments.pkl                        # Final trained model
├── README.md                           # Project documentation
└── .gitignore
```

---

## 🚀 Technologies Used

| Category | Technology |
|---|---|
| Programming Language | Python |
| Machine Learning | Scikit-learn, XGBoost |
| Data Processing | NumPy, Pandas |
| Visualization | Matplotlib, Seaborn |
| Web Framework | Flask |
| Frontend | HTML, CSS |
| Model Storage | Pickle (.pkl) |
| Environment | Jupyter Notebook, VS Code |

---

## ⚙️ System Workflow

1. Load payment transaction dataset  
2. Clean and preprocess data  
3. Train fraud detection model  
4. Save trained model (`payments.pkl`)  
5. Flask app loads model  
6. User enters transaction details  
7. System predicts fraud or not fraud  

---

## 🛠️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/KrupaJakka/SmartBridge_online_payment_fraud_detection_using_machine_learning
cd online-payments-fraud-detection
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

#### Activate Environment

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

---

### 3️⃣ Install Required Libraries

```bash
pip install numpy pandas scikit-learn xgboost flask matplotlib seaborn
```

---

### 4️⃣ Train the Model (If Needed)

Open notebook:

```
training/ONLINE PAYMENTS FRAUD DETECTION.ipynb
```

Run all cells → generates:

```
payments.pkl
```

Move the model to:

```
flask/
```

---

### 5️⃣ Run the Flask Application

```bash
cd flask
python app.py
```

---

### 6️⃣ Open in Browser

```
http://127.0.0.1:5000
```

Enter transaction details → get fraud prediction.

---

## 👤 Author

**JAKKA KRUPA RATNAM**  
B.Tech CSE (IoT)

