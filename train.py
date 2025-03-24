import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder

def train_anomaly_model(csv_file):
    df = pd.read_csv(csv_file)
    
    # Clean numerical columns
    numerical_cols = ['duration_(secs)', 'bytes', 'age', 'sales']
    for col in numerical_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df.dropna(subset=numerical_cols, inplace=True)
    
    # Clean categorical columns
    categorical_cols = ['network_protocol', 'accessed_Ffom', 'country', 'pay_method']
    df[categorical_cols] = df[categorical_cols].replace('--', 'Unknown')
    
    # Encode categoricals
    encoder = LabelEncoder()
    for col in categorical_cols:
        df[col] = encoder.fit_transform(df[col].astype(str))
    
    # Train model
    features = numerical_cols + categorical_cols
    X = df[features]
    model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
    df["Anomaly"] = model.fit_predict(X)
    
    df.to_csv("anomalies_detected.csv", index=False)
    print("Anomaly detection completed!")

train_anomaly_model("anonymized_logs.csv")
