import pandas as pd
import matplotlib.pyplot as plt

# Load results
df = pd.read_csv("anomalies_detected.csv")

# 1. Basic Anomaly Analysis
anomalies = df[df["Anomaly"] == -1]
total_anomalies = len(anomalies)
fraud_correlation = anomalies["returned"].value_counts(normalize=True)
fraud_rate = fraud_correlation.get('Yes', 0)*100

print(f"Security Alert Summary:")
print(f"- Total anomalies detected: {total_anomalies}")
print(f"- Anomalies linked to returns/fraud: {fraud_rate:.2f}%")

# 2. High-Risk Transaction Detection
high_risk = anomalies[
    (anomalies["bytes"] > 100000) & 
    (anomalies["sales"] < 10)
]

print("\nHigh-risk transactions (potential data exfiltration):")
print(high_risk[["ip", "bytes", "sales", "returned", "network_protocol", "country"]])

# 3. Zero-Sale High-Bandwidth Detection
critical_risk = df[
    (df["bytes"] > 300000) & 
    (df["sales"] == 0)
]

print("\nCritical alerts (zero-sale, high bandwidth):")
print(critical_risk[["ip", "network_protocol", "country", "pay_method", "duration_(secs)"]])

# 4. Visualization
plt.figure(figsize=(12, 6))

# Plot all transactions
plt.scatter(df['sales'], df['bytes'], 
            c=df['Anomaly'].map({1: 'blue', -1: 'red'}),
            alpha=0.6,
            label='Normal (Blue) vs Anomaly (Red)')

# Highlight critical risks
plt.scatter(critical_risk['sales'], critical_risk['bytes'],
            c='yellow', edgecolors='black',
            s=200, marker='X',
            label='Critical Alerts')

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Sales Amount (log scale)')
plt.ylabel('Bytes Transferred (log scale)')
plt.title('Network Security Threat Detection\n(Anomalies vs Sales Activity)')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.tight_layout()

# Save visualization
plt.savefig('threat_detection_visualization.png')
print("\nSaved security visualization to 'threat_detection_visualization.png'")

# 5. Export Critical Alerts
critical_risk.to_csv('critical_alerts.csv', index=False)
print("Saved critical alerts to 'critical_alerts.csv'")

# 6. Security Recommendations
print("\nRecommended Actions:")
print("- Block IPs with repeated high-bandwidth, zero-sale transactions")
print("- Investigate protocol usage for critical alerts")
print("- Review payment methods used in anomalous transactions")
print("- Implement rate limiting for high-bandwidth connections")
