# 📊 Customer Churn Prediction using Machine Learning

## 📌 Project Overview
Customer churn refers to customers stopping the use of a company’s services. Since retaining existing customers is more cost-effective than acquiring new ones, churn prediction is critical for business growth.

This project predicts customer churn using machine learning by analyzing customer demographics, service usage, and billing information.

---

## 🎯 Objective
- Predict whether a customer will churn or stay
- Identify key factors influencing churn
- Help businesses design data-driven retention strategies

---

## 📂 Dataset Description
The dataset contains customer-level information including:
- Demographic details
- Service subscription data
- Account and billing information

### Key Features
- Gender
- SeniorCitizen
- Tenure
- MonthlyCharges
- Contract Type
- Payment Method

### Target Variable
- **Churn**
  - Yes → Customer left
  - No → Customer stayed

---

## 🧠 Machine Learning Workflow
1. Data Loading
2. Exploratory Data Analysis (EDA)
3. Data Preprocessing
   - Handling missing values
   - Encoding categorical variables
   - Feature scaling
4. Model Training
5. Model Evaluation
6. Prediction

---

## 🤖 Models Used
- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

✅ **Random Forest achieved the best performance** based on evaluation metrics.

---

## 📈 Model Performance
- **Accuracy:** ~79%
- Precision, Recall, and F1-score were used for detailed evaluation
- Confusion Matrix used to analyze misclassifications

📌 The model performs well in identifying non-churn customers and reasonably predicts churned customers.

---

## 💡 Business Insights
- Customers with low tenure are more likely to churn
- Higher monthly charges increase churn probability
- Long-term contracts reduce churn risk

These insights can help companies improve retention strategies.

---

## 🛠️ Technologies & Tools
- **Language:** Python
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
- **IDE:** VS Code
- **Version Control:** Git & GitHub

---

## 🚀 How to Run the Project
```bash
git clone https://github.com/Newshika28/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction
pip install -r requirements.txt
jupyter notebook
