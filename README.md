# Network-Intrusion-Detection-System 🚨

# 🛡️ Business Domain
Cybersecurity

## 😥 Problem Statement
Every day, companies receive millions of network requests from employees, customers, and hackers. It is impossible for security teams to manually inspect every network connection.

The goal of this project is to build a Network Intrusion Detection System that automatically analyzes network traffic and predicts whether a network connection is Normal or Malicious. This helps organizations detect cyberattacks early and protect their systems from unauthorized access.

## 🎯 Business Objective
Developed a system that automatically detects malicious network traffic using historical network flow data, enabling security teams to identify cyber threats quickly and minimize potential damage.

## 📊 Data Source
[!Intrusion Detection (CICIDS2017 )](https://www.kaggle.com/datasets/elshewey/intrusion-detection-cicids2017)

## 😜 Dataset Summary
Input Features (X): 51 numerical features
Target Variable (y): Attack_Binary
Problem Type: Binary Classification
Algorithm: Artificial Neural Network (ANN)

## 🤔 Why ANN?
This dataset is ideal for an ANN because all predictors are numerical, so after preprocessing (handling missing values if any and feature scaling), they can be fed directly into a fully connected neural network for binary classification.