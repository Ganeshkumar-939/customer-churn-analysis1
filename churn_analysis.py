# ============================================================
# CUSTOMER CHURN ANALYSIS - TELECOM INDUSTRY
# Author: Venkata Ganesh Kumar Nethuluri
# Email: ganeshkumarnethuluri@gmail.com
# GitHub: https://github.com/Ganeshkumar-939
# ============================================================
# HOW TO USE:
# 1. Go to https://colab.research.google.com
# 2. Click File > New Notebook
# 3. Copy-paste each section into separate cells
# 4. Run each cell one by one
# ============================================================

# ── CELL 1: Install & Import Libraries ─────────────────────
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, classification_report,
                             confusion_matrix, ConfusionMatrixDisplay)
import warnings
warnings.filterwarnings('ignore')

print("✅ All libraries imported successfully!")

# ── CELL 2: Load Dataset ────────────────────────────────────
# Download from: https://www.kaggle.com/datasets/blastchar/telco-customer-churn
# Upload to Colab when prompted

from google.colab import files
uploaded = files.upload()   # select telco_churn.csv

df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
print(f"Dataset Shape: {df.shape}")
print(f"\nFirst 5 rows:")
df.head()

# ── CELL 3: Data Overview ───────────────────────────────────
print("=== DATASET INFO ===")
print(df.info())
print("\n=== MISSING VALUES ===")
print(df.isnull().sum())
print("\n=== CHURN DISTRIBUTION ===")
print(df['Churn'].value_counts())
print(f"\nChurn Rate: {df['Churn'].value_counts(normalize=True)['Yes']*100:.1f}%")

# ── CELL 4: Data Cleaning ───────────────────────────────────
# Fix TotalCharges column (has spaces)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)

# Convert Churn to binary
df['Churn_Binary'] = df['Churn'].map({'Yes': 1, 'No': 0})

# Drop CustomerID
df.drop('customerID', axis=1, inplace=True)

print("✅ Data cleaning complete!")
print(f"Shape after cleaning: {df.shape}")

# ── CELL 5: EDA - Churn Distribution ───────────────────────
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Pie chart
churn_counts = df['Churn'].value_counts()
colors = ['#2ecc71', '#e74c3c']
axes[0].pie(churn_counts, labels=churn_counts.index, autopct='%1.1f%%',
            colors=colors, startangle=90, textprops={'fontsize': 13})
axes[0].set_title('Overall Churn Distribution', fontsize=14, fontweight='bold')

# Bar chart
sns.countplot(data=df, x='Churn', palette={'No': '#2ecc71', 'Yes': '#e74c3c'},
              ax=axes[1])
axes[1].set_title('Churn Count', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Churn Status')
axes[1].set_ylabel('Number of Customers')
for p in axes[1].patches:
    axes[1].annotate(f'{int(p.get_height())}',
                     (p.get_x() + p.get_width() / 2., p.get_height()),
                     ha='center', va='bottom', fontsize=12)

plt.tight_layout()
plt.savefig('churn_distribution.png', dpi=150, bbox_inches='tight')
plt.show()
print("✅ Chart saved!")

# ── CELL 6: Churn by Contract Type ─────────────────────────
plt.figure(figsize=(10, 6))
contract_churn = df.groupby('Contract')['Churn_Binary'].mean() * 100

bars = plt.bar(contract_churn.index, contract_churn.values,
               color=['#3498db', '#e67e22', '#e74c3c'], edgecolor='black')
plt.title('Churn Rate by Contract Type', fontsize=15, fontweight='bold', pad=15)
plt.xlabel('Contract Type', fontsize=12)
plt.ylabel('Churn Rate (%)', fontsize=12)
plt.ylim(0, 55)

for bar, val in zip(bars, contract_churn.values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
             f'{val:.1f}%', ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('churn_by_contract.png', dpi=150, bbox_inches='tight')
plt.show()

# ── CELL 7: Churn by Tenure ─────────────────────────────────
df['Tenure_Group'] = pd.cut(df['tenure'],
                             bins=[0, 12, 24, 48, 72],
                             labels=['0-12 months', '13-24 months',
                                     '25-48 months', '49-72 months'])

tenure_churn = df.groupby('Tenure_Group')['Churn_Binary'].mean() * 100

plt.figure(figsize=(10, 6))
bars = plt.bar(tenure_churn.index, tenure_churn.values,
               color=['#e74c3c', '#e67e22', '#f1c40f', '#2ecc71'],
               edgecolor='black')
plt.title('Churn Rate by Customer Tenure', fontsize=15, fontweight='bold', pad=15)
plt.xlabel('Tenure Group', fontsize=12)
plt.ylabel('Churn Rate (%)', fontsize=12)
plt.ylim(0, 60)

for bar, val in zip(bars, tenure_churn.values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
             f'{val:.1f}%', ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('churn_by_tenure.png', dpi=150, bbox_inches='tight')
plt.show()

# ── CELL 8: Churn by Internet Service ───────────────────────
plt.figure(figsize=(10, 6))
internet_churn = df.groupby('InternetService')['Churn_Binary'].mean() * 100
colors_map = {'DSL': '#3498db', 'Fiber optic': '#e74c3c', 'No': '#2ecc71'}
colors_list = [colors_map[x] for x in internet_churn.index]

bars = plt.bar(internet_churn.index, internet_churn.values,
               color=colors_list, edgecolor='black')
plt.title('Churn Rate by Internet Service Type', fontsize=15, fontweight='bold')
plt.xlabel('Internet Service', fontsize=12)
plt.ylabel('Churn Rate (%)', fontsize=12)
plt.ylim(0, 55)

for bar, val in zip(bars, internet_churn.values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
             f'{val:.1f}%', ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('churn_by_internet.png', dpi=150, bbox_inches='tight')
plt.show()

# ── CELL 9: Monthly Charges vs Churn ────────────────────────
plt.figure(figsize=(10, 6))
df.boxplot(column='MonthlyCharges', by='Churn',
           patch_artist=True,
           boxprops=dict(facecolor='#3498db', alpha=0.6),
           medianprops=dict(color='red', linewidth=2))
plt.title('Monthly Charges by Churn Status', fontsize=14, fontweight='bold')
plt.suptitle('')
plt.xlabel('Churn Status')
plt.ylabel('Monthly Charges ($)')
plt.tight_layout()
plt.savefig('charges_vs_churn.png', dpi=150, bbox_inches='tight')
plt.show()

# ── CELL 10: Machine Learning Model ─────────────────────────
# Encode categorical variables
df_model = df.copy()
le = LabelEncoder()
cat_cols = df_model.select_dtypes(include='object').columns

for col in cat_cols:
    df_model[col] = le.fit_transform(df_model[col].astype(str))

# Features and Target
X = df_model.drop(['Churn', 'Churn_Binary'], axis=1)
y = df_model['Churn_Binary']

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

print(f"Training samples: {X_train.shape[0]}")
print(f"Testing samples:  {X_test.shape[0]}")

# ── CELL 11: Train Models ───────────────────────────────────
# Logistic Regression
lr = LogisticRegression(max_iter=1000, random_state=42)
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)
lr_acc = accuracy_score(y_test, lr_pred)

# Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
rf_acc = accuracy_score(y_test, rf_pred)

print("=" * 45)
print(f"  Logistic Regression Accuracy : {lr_acc*100:.2f}%")
print(f"  Random Forest Accuracy       : {rf_acc*100:.2f}%")
print("=" * 45)

print("\n📋 Random Forest Classification Report:")
print(classification_report(y_test, rf_pred, target_names=['No Churn', 'Churn']))

# ── CELL 12: Confusion Matrix ───────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

for ax, model, pred, name in zip(
        axes,
        [lr, rf],
        [lr_pred, rf_pred],
        ['Logistic Regression', 'Random Forest']):
    cm = confusion_matrix(y_test, pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                                  display_labels=['No Churn', 'Churn'])
    disp.plot(ax=ax, colorbar=False, cmap='Blues')
    ax.set_title(f'{name}\nAccuracy: {accuracy_score(y_test, pred)*100:.1f}%',
                 fontsize=13, fontweight='bold')

plt.tight_layout()
plt.savefig('confusion_matrix.png', dpi=150, bbox_inches='tight')
plt.show()

# ── CELL 13: Feature Importance ─────────────────────────────
feat_imp = pd.Series(rf.feature_importances_, index=X.columns)
feat_imp = feat_imp.sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
bars = plt.barh(feat_imp.index[::-1], feat_imp.values[::-1],
                color='#3498db', edgecolor='black')
plt.title('Top 10 Features Driving Churn', fontsize=14, fontweight='bold')
plt.xlabel('Feature Importance Score', fontsize=12)
plt.tight_layout()
plt.savefig('feature_importance.png', dpi=150, bbox_inches='tight')
plt.show()

# ── CELL 14: Summary ────────────────────────────────────────
print("=" * 55)
print("         PROJECT SUMMARY - CHURN ANALYSIS")
print("=" * 55)
print(f"  Total Customers Analyzed  : {len(df):,}")
print(f"  Overall Churn Rate        : {df['Churn_Binary'].mean()*100:.1f}%")
print(f"  Best Model                : Random Forest")
print(f"  Best Model Accuracy       : {rf_acc*100:.2f}%")
print("=" * 55)
print("\n💡 KEY BUSINESS INSIGHTS:")
print("  1. Month-to-month contracts → Highest churn risk")
print("  2. New customers (< 12 months) → Need early retention")
print("  3. Fiber optic users → Churn due to pricing")
print("  4. Electronic check payers → Target for auto-pay switch")
print("  5. Senior citizens → Need dedicated support program")
print("\n✅ Analysis Complete!")
