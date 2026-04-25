# 🏦 Mule Account Detection System (Maestro Fintech)

## 📌 Project Overview
This project serves as a robust second line of defense against synthetic identity fraud (deepfakes). While traditional KYC handles onboarding, this Machine Learning microservice analyzes the transactional footprint—specifically the high-velocity inflows and outflows characteristic of money mule networks. 

## 🏗️ Architecture & Tech Stack
* **Machine Learning:** TensorFlow, Keras (Deep Neural Network), Scikit-Learn, Pandas.
* **API Development:** Flask, Python 3.10.
* **Cloud & DevOps:** Docker, AWS EC2 (t2.medium), Ubuntu.

## 📊 Model Performance
Trained on the highly imbalanced PaySim dataset (6.3M records), the model was heavily optimized to minimize False Negatives via Class Weighting and Early Stopping.
* **ROC-AUC:** 0.992
* **Recall:** 94.5% (Successfully catches 94.5% of all mule transactions)
* **F1-Score:** 0.792

## 🚀 How to Run the Live API (Docker)
This model is packaged as a production-ready microservice. To spin up the inference API locally or on a cloud server:

1. **Clone the repository:**
   `git clone https://github.com/nwosumajor/mule-detection-system.git`
2. **Build the Docker Image:**
   `docker build -t mule-api:latest ./api`
3. **Run the Container:**
   `docker run -d -p 5000:5000 mule-api:latest`
4. **Test the Endpoint:**
   ```bash
   curl -X POST http://localhost:5000/predict-mule \
   -H "Content-Type: application/json" \
   -d '{"amount": 50000, "oldbalanceOrg": 50000, "newbalanceOrig": 0, "type_CASH_OUT": 1}'
