# 📊 Customer Churn Analysis — Telecom Industry

**Tools:** Python | SQL | Excel | Tableau  
**Domain:** Telecom | Customer Retention  
**Level:** Data Analyst Portfolio Project  
**Author:** Venkata Ganesh Kumar Nethuluri  
**Email:** ganeshkumarnethuluri@gmail.com  
**GitHub:** https://github.com/Ganeshkumar-939

---

## 🎯 Objective

Analyze telecom customer data to identify key churn drivers and build a predictive model to help the business reduce customer attrition and improve retention strategy.

---

## ❓ Business Problem

A telecom company is losing customers every month. The business team wants to know:
- **Who** is most likely to churn?
- **Why** are they leaving?
- **What** actions can reduce churn?

---

## 📁 Project Structure

```
customer-churn-analysis/
│
├── README.md                  ← You are here
├── data/
│   └── telco_churn.csv        ← Dataset (IBM Telco)
├── notebooks/
│   └── churn_analysis.ipynb   ← Full Python EDA + Model
├── sql/
│   └── churn_queries.sql      ← SQL analysis queries
├── dashboard/
│   └── churn_dashboard.png    ← Tableau dashboard screenshot
└── images/
    ├── churn_by_contract.png
    ├── churn_by_tenure.png
    └── confusion_matrix.png
```

---

## 🔍 Key Findings

| Insight | Finding |
|---|---|
| Contract Type | Month-to-month customers churn **42%** vs 11% annual |
| Tenure | Customers with **< 12 months** tenure are highest risk |
| Internet Service | Fiber optic users churn at **41.9%** |
| Payment Method | Electronic check users churn most (**45%**) |
| Senior Citizens | Churn rate **41%** vs 24% for non-seniors |

---

## 🛠️ Tools & Libraries Used

```python
pandas        # Data cleaning and manipulation
numpy         # Numerical operations
matplotlib    # Charts and graphs
seaborn       # Statistical visualizations
scikit-learn  # Machine learning model
SQL           # Data querying and aggregation
Excel         # Pivot tables and summary
```

---

## 🤖 Model Performance

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---|---|---|---|
| Logistic Regression | 80.2% | 0.67 | 0.55 | 0.60 |
| Random Forest | **82.1%** | **0.71** | **0.58** | **0.64** |

**Best Model:** Random Forest Classifier

---

## 💡 Business Recommendations

1. **Offer annual contract discounts** to month-to-month customers in first 3 months
2. **Target fiber optic users** with loyalty rewards
3. **Senior citizen retention program** — dedicated support line
4. **Electronic check users** — incentivize auto-pay switch
5. **Early intervention at 6-month mark** for high-risk customers

---

## 📊 Dashboard Preview

> Dashboard built in Tableau showing churn by contract, payment method, and tenure bands.

![Churn Dashboard](dashboard/churn_dashboard.png)

---

## 📂 Dataset Source

- **Dataset:** IBM Telco Customer Churn  
- **Source:** [Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)  
- **Rows:** 7,043 customers | **Columns:** 21 features

---

## 🚀 How to Run

```bash
# 1. Clone the repository
git clone https://github.com/Ganeshkumar-939/customer-churn-analysis

# 2. Open Google Colab or Jupyter Notebook
# Upload churn_analysis.ipynb

# 3. Upload telco_churn.csv when prompted

# 4. Run all cells (Runtime > Run All)
```

---

## 📜 Related Certifications

- ✅ Deloitte Data Analytics Job Simulation (Forage, Dec 2025)
- ✅ Cisco Data Analytics Essentials (Dec 2025)
- ✅ micro1 Certified Entry-level Data Analyst (Jan 2026)
- ✅ Business Analytics with Excel

---

*This project was built as part of my data analyst portfolio to demonstrate real-world data analysis skills.*
