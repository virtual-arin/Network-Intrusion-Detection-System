# Network Intrusion Detection System 🔐

## 🛡️ Business Domain
Cybersecurity

## 🤔 Problem Statement
Modern organizations generate millions of network connections every day. Among them, some are malicious and can lead to cyberattacks, data breaches, and unauthorized access. Manually inspecting every network connection is impractical due to the massive volume of traffic.

This project develops an Artificial Neural Network (ANN) based Intrusion Detection System that automatically classifies network traffic as **Normal** or **Attack**, helping organizations detect threats quickly and improve network security.

## 🎯 Project Objective
The objective of this project is to build a binary classification model using an Artificial Neural Network (ANN) that predicts whether a network connection is **Normal Traffic** or **Attack Traffic** based on network flow features.

## 📊 Data Source
**Dataset:** [Intrusion Detection (CICIDS2017)](https://www.kaggle.com/datasets/elshewey/intrusion-detection-cicids2017)

## 📈 Dataset Overview
- **Input Features:** 52 Numerical Features
- **Target Variable:** `Attack_Binary`
- **Problem Type:** Binary Classification
- **Algorithm:** Artificial Neural Network (ANN)

## 🛠️ Tech Stack
- **Language:** Python
- **Libraries:** NumPy, Pandas, Matplotlib, Seaborn
- **Deep Learning:** TensorFlow, Keras
- **Machine Learning:** Scikit-learn
- **Model Storage:** Joblib
- **Web App:** Streamlit
- **Environment:** Jupyter Notebook / VS Code

## 📂 Project Structure
```text
├── models/
│   ├── network_intrusion_detection_ann.keras
│   └── scaler.pkl
├── notebooks/
│   └── Notebook.ipynb
├── Test Data/
│   └── sample_network_data.csv
├── .gitignore
├── app.py
├── LICENSE
├── README.md
└── requirements.txt
```

## 🔄 Project Workflow
1. Data Cleaning & Preprocessing
2. Exploratory Data Analysis (EDA)
3. Feature Scaling using StandardScaler
4. Train-Test Split
5. ANN Model Building & Training
6. Model Evaluation
7. Model Saving
8. Streamlit Application Development

## 📊 Model Performance

| Metric | Score |
|--------|------:|
| Test Accuracy | **98.38%** |
| Precision | **98–99%** |
| Recall | **98–99%** |
| F1-Score | **98%** |

## 🚀 Streamlit Application
The application allows users to:
- Upload a CSV file containing network traffic records.
- Predict whether each record is **Normal Traffic** or **Attack Traffic**.
> **💡 Note:** To test the application, use the sample CSV file available in the **`Test Data/`** folder (`sample_network_data.csv`).

## 🔮 Future Improvements
- Multi-class attack classification
- Hyperparameter tuning
- Real-time intrusion detection
- Cloud deployment
- REST API integration