# SecureCart: AI-Powered Fraud Detection for E-commerce Network Logs

## Overview

This project implements an end-to-end network security solution for detecting fraudulent transactions and suspicious activities in e-commerce logs. Using Google Cloud's Data Loss Prevention (DLP) for data anonymization and Isolation Forest machine learning model for anomaly detection, the system identifies high-risk patterns including potential data exfiltration and fraudulent returns.

## Key Components

✅ **Data Anonymization**: Protects PII using Google DLP  
✅ **AI-Powered Detection**: Isolation Forest model flags suspicious transactions  
✅ **Security Analytics**: Identifies high-risk patterns (zero-sale/high-bandwidth activities)  
✅ **Actionable Outputs**: CSV reports and visualizations for security teams

## Team Members

- Uche
- Mat

## Features

- `dlp.py`: Automated sensitive data redaction
- `train.py`: Machine learning pipeline for anomaly detection
- `analyze.py`: Security insights generation with visual reporting
- Sample dataset for demonstration

## Technical Requirements

- Python 3.8+
- Google Cloud Platform account (DLP API enabled)
- Libraries: pandas, scikit-learn, matplotlib, google-cloud-dlp

## Installation

```bash
git clone https://github.com/yourusername/ecommerce-fraud-detection.git
cd ecommerce-fraud-detection
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows
pip install -r requirements.txt

# Configure Google Cloud credentials
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-key.json"
```

## Usage

1. **Data Anonymization**:

```bash
python dlp.py --project=your-gcp-project-id \
              --input=input_data.csv \
              --output=anonymized_data.csv \
              --fields=ip,email
```

2. **Train Anomaly Detection Model**:

```bash
python train.py anonymized_data.csv
```

3. **Generate Security Insights**:

```bash
python analyze.py
```

Sample dataset included for demonstration purposes.

## Technical Paper Outline (4 Pages)

### Title Page

- **Title**: "SecureCart: Machine Learning Approach for E-commerce Fraud Detection"
- **Team Members**: [Your Names]
- **Abstract**: 150-word summary of methodology and key findings

### 1. Introduction

- Problem statement: Growing e-commerce fraud challenges
- Objectives: Automated detection of suspicious transactions

### 2. Background

- Network security in e-commerce
- Isolation Forest algorithm overview
- Data privacy considerations (DLP)

### 3. Methodology

- Data collection & preprocessing (Fig 1: Architecture Diagram)
- Feature engineering: bytes/sec, protocol encoding
- Model training process

### 4. Results

- Detection accuracy metrics
- Case study: High-risk transaction analysis
- Visualization: Sales vs. Bandwidth plot

### 5. Conclusion

- Key findings: 4.39% fraud correlation
- Future work: Real-time monitoring system
