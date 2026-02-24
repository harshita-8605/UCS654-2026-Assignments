# Data Generation using Modelling and Simulation for Machine Learning

## Introduction

This assignment focuses on generating synthetic data using modelling and simulation, and then using that data to train and compare different machine learning models. Instead of using an existing dataset, a mathematical simulation is used to generate realistic data, which is then treated as input for ML models.

---

## Simulation Tool Used

A physics-based simulation was implemented using **Python and NumPy**. The system simulated is **projectile motion**, where output values are generated using mathematical equations by randomly varying input parameters. This approach follows the concept of modelling and simulation commonly used for synthetic data generation.

---

## Data Generation Methodology

Random values were generated within the defined bounds for each input parameter. These values were passed into the mathematical equations of projectile motion to calculate the output range. Small random noise was added to make the data more realistic.
A total of **1000 simulations** were generated, forming a synthetic dataset.

---

## Machine Learning Models Used

The generated dataset was treated as a regression problem, where the goal was to predict projectile range.

The following models were trained and compared:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* K-Nearest Neighbors
* Support Vector Regressor

---

## Evaluation Metrics

Models were evaluated using:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² Score

Lower error values and higher R² indicate better performance.

---

## Results

### Result Table

A comparison table was generated showing MAE, RMSE, and R² score for each model. The models were ranked based on R² score, and the best-performing model achieved the highest R² value with the lowest prediction error.

(Exact values are shown in the Colab notebook output.)

---

## Result Graphs

* A bar graph was plotted to compare R² scores of all models.
* A scatter plot of actual vs predicted values was plotted for the best model.

These graphs help visualize model performance and prediction accuracy clearly.

---

## Conclusion

Using simulation-based data generation, a complete machine learning pipeline was implemented. Among the compared models, the model with the highest R² score performed best on the simulated dataset. This assignment demonstrates how modelling and simulation can be effectively used to generate data for machine learning tasks and evaluate multiple models systematically.

---

## Tools Used

* Python
* NumPy
* Pandas
* Matplotlib
* Scikit-learn
* Google Colab
