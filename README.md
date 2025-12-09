#  Predictive Maintenance

This project focuses on building a Predictive Maintenance model that anticipates machine failure based on historical sensor and operational data.  
It helps in optimizing maintenance schedules, reducing downtime, and improving operational efficiency.

---

##  Objective

To predict whether a machine will fail in the near future using:

- Machine operating conditions  
- Sensor readings  
- Maintenance logs  
- Failure types  

##  Dataset Description

| Feature | Description |
|---------|-------------|
| machine_id | Unique machine identifier |
| age | Machine age in years |
| operation_hours | Total hours in operation |
| temperature | Real-time temperature sensor |
| pressure | Pressure readings |
| vibration | Vibration signal data |
| maintenance_type | Preventive/Corrective |
| failure | Target variable (0 = No Failure, 1 = Failure) |

---

##  Data Preprocessing Steps

✔ Handling missing values  
✔ Feature encoding & scaling  
✔ Outlier detection using IQR  
✔ Feature correlation analysis  
✔ Splitting dataset (Train/Test)

---

##  Machine Learning Models Used

| Model | Purpose | Result |
|--------|---------|---------|
| Logistic Regression | Baseline classification |  Moderate accuracy |
| Random Forest | Feature importance + prediction |  Best performance |
| XGBoost | Optimized failure prediction |  Highest accuracy |

---

##  Model Evaluation Metrics

- Accuracy  
- Precision  
- Recall  
- F1-score  
- ROC–AUC Curve  
- Confusion Matrix




