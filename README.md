# Credit Card Fraud Detection : Sampling & Model Comparison

## Overview

This project focuses on analyzing a **highly imbalanced credit card fraud dataset** and studying how **different sampling techniques** affect the performance of multiple **machine learning classification models**.

The workflow follows four major steps:

1. Data understanding and imbalance handling
2. Dataset sampling using multiple strategies
3. Model training on sampled datasets
4. Performance comparison using accuracy metrics

The objective is **not** to maximize accuracy, but to **compare how sampling strategies influence model behavior**.

---

## Dataset Description

* Dataset: Credit Card Transactions
* Target variable: `Class`

  * `0` → Non-fraudulent transaction
  * `1` → Fraudulent transaction
* The dataset is **extremely imbalanced**, with fraud cases forming a very small minority.

---

## Methodology

### 1. Handling Class Imbalance

The original dataset had a very small number of fraud samples. Direct oversampling from the minority class would introduce excessive synthetic data and degrade quality.

To address this:

* **Random undersampling** was first applied to the majority class.
* **SMOTE (Synthetic Minority Oversampling Technique)** was then used to generate additional minority samples.

This hybrid approach balances the dataset while preserving meaningful structure.

---

### 2. Sampling Techniques (Task 3)

After balancing, **five different samples** were created from the dataset using different sampling strategies:

#### a. Simple Random Sampling

* Randomly selects a fixed fraction of data.
* Does not preserve class distribution explicitly.

#### b. Stratified Sampling

* Ensures the class distribution (`Class`) remains consistent with the original dataset.
* Useful for imbalanced classification problems.

#### c. Cluster Sampling

* Data was grouped into clusters based on the `Time` feature.
* Entire clusters were selected, and then a fraction was sampled.
* Helps analyze model behavior when trained on grouped data.

#### d. Systematic Sampling

* Samples every *k-th* observation from the dataset.
* Ensures uniform coverage across the dataset.

#### e. Bootstrap Sampling

* Sampling performed **with replacement**.
* Same observation may appear multiple times.
* Useful for studying model stability.

---

### 3. Machine Learning Models (Task 4)

Each sampling method was evaluated using the **same five classification models**:

1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier
4. Support Vector Machine (SVM)
5. K-Nearest Neighbors (KNN)

All models were trained and evaluated **on the same sampled dataset** to ensure fair comparison across sampling strategies.

---

## Evaluation Metric

### Accuracy

Accuracy was used as the evaluation metric:

[
Accuracy = \frac{\text{Correct Predictions}}{\text{Total Predictions}}
]

Since the assignment did not specify a train–test split, accuracy was calculated **on the sampled data itself** to allow direct comparison between sampling techniques.

---

## Results

### Accuracy Matrix

Model performance across sampling techniques is summarized in the accuracy matrix:

| Model               | Random | Stratified | Cluster | Systematic | Bootstrap |
| ------------------- | ------ | ---------- | ------- | ---------- | --------- |
| Logistic Regression | …      | …          | …       | …          | …         |
| Decision Tree       | …      | …          | …       | …          | …         |
| Random Forest       | …      | …          | …       | …          | …         |
| SVM                 | …      | …          | …       | …          | …         |
| KNN                 | …      | …          | …       | …          | …         |

*(Values are filled programmatically in the notebook)*

---

## Observations

* Decision Tree and Random Forest models showed consistently high accuracy across all sampling techniques.
* Stratified sampling produced stable results by maintaining class balance.
* Cluster and bootstrap sampling introduced some variation depending on data composition.
* KNN was more sensitive to changes in sampling strategy compared to other models.

## Conclusion

* Sampling technique has a noticeable impact on model performance.
* No single sampling method performs best for all models.
* Effective sampling is crucial when working with imbalanced datasets.

---

## Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* Imbalanced-learn (SMOTE)
* Jupyter Notebook

---

## Author Notes

This notebook reflects an iterative problem-solving approach, including experimentation with different sampling strategies and model behaviors.
