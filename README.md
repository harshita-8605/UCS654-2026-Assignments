# TOPSIS Based Selection of Sentence Similarity Model

## Introduction

This assignment applies the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method to select the best pre-trained model for the **Sentence Similarity** task. Instead of relying only on accuracy, multiple criteria are considered to make a balanced and practical decision.

---

## Objective

To identify the most suitable pre-trained sentence similarity model using a multi-criteria decision-making approach.

---

## Models Used

* SBERT
* Universal Sentence Encoder (USE)
* MiniLM
* MPNet
* DistilBERT

---

## Methodology (TOPSIS)

1. A decision matrix was created using model performance values.
2. The matrix was normalized to remove scale differences.
3. Weights were applied to each criterion.
4. Ideal best and ideal worst solutions were identified.
5. Distances from ideal best and worst were calculated.
6. TOPSIS scores were computed and models were ranked.

The model with the highest TOPSIS score is considered the best.

---

## Result Graph

A bar graph was plotted to visualize TOPSIS scores of all models. The graph clearly highlights the top-ranked model and makes comparison easier than using tables alone.

---

## Conclusion

Using TOPSIS, the best pre-trained model for sentence similarity was selected by considering performance, efficiency, and computational cost together. This approach provides a more reliable model selection compared to using a single metric.

---

## Tools Used

Python, NumPy, Pandas, Matplotlib, Google Colab
