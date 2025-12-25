# Credit Card Fraud Detection

A machine learning project that uses Logistic Regression to detect fraudulent credit card transactions. The model is trained on an imbalanced dataset with class weighting to improve fraud detection accuracy.

## Overview

Credit card fraud is a significant problem for financial institutions and customers. This project implements a supervised learning approach to identify fraudulent transactions based on historical transaction data.

## Dataset

The project uses the **Credit Card Fraud Detection Dataset** which contains:
- **284,807 transactions** made by European cardholders in September 2013
- **Highly imbalanced**: Only 0.172% of transactions are fraudulent
- **30 features**: 28 anonymized features (V1-V28) obtained through PCA transformation, plus 'Time' and 'Amount'
- **Target variable**: 'Class' (0 = Legitimate, 1 = Fraudulent)

> **Note**: The dataset file `creditcard.csv` is not included in this repository due to its size and privacy considerations.

## Features

- **Data Exploration**: Visualize class distribution and analyze imbalanced data
- **Feature Scaling**: StandardScaler normalization for improved model performance
- **Stratified Splitting**: Maintains class distribution in train/test sets
- **Class Weighting**: Handles imbalanced data by assigning higher weights to minority class
- **Model Evaluation**: Comprehensive metrics including confusion matrix, classification report, and ROC-AUC score
- **Visualization**: Heatmap visualization of model predictions

## Installation

### Prerequisites

```bash
Python 3.7+
```

### Required Libraries

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

## Usage

1. Clone the repository:
```bash
git clone https://github.com/MathewX470/ML-Projects.git
cd ML-Projects
```

2. Download the Credit Card Fraud Detection dataset from [Kaggle](https://www.kaggle.com/mlg-ulb/creditcardfraud) and place `creditcard.csv` in the project directory.

3. Open the Jupyter notebook:
```bash
jupyter notebook credit_card__fraud_detection_isolation_forest.ipynb
```

4. Run all cells to train the model and see results.

## Model Details

### Algorithm: Logistic Regression

**Hyperparameters:**
- `max_iter=1000`: Maximum iterations for convergence
- `class_weight='balanced'`: Automatically adjusts weights to handle imbalanced data
- `random_state=42`: Ensures reproducibility

### Data Preprocessing

1. **Train-Test Split**: 80% training, 20% testing with stratification
2. **Feature Scaling**: StandardScaler applied to normalize features

### Evaluation Metrics

- **Confusion Matrix**: Shows true positives, true negatives, false positives, and false negatives
- **Classification Report**: Precision, recall, F1-score for both classes
- **ROC-AUC Score**: Measures model's ability to distinguish between classes

## Results

The model achieves high accuracy in detecting fraudulent transactions while minimizing false positives. Detailed performance metrics are available in the notebook output.
