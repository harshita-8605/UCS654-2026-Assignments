import pandas as pd
import numpy as np

def topsis(input_file, weights, impacts, output_file):
    df = pd.read_csv(input_file)
    data = df.iloc[:, 1:].astype(float)

    weights = [float(w) for w in weights.split(",")]
    impacts = impacts.split(",")

    norm = data.copy()
    for col in range(data.shape[1]):
        denom = 0
        for val in data.iloc[:, col]:
            denom += val * val
        denom = denom ** 0.5
        norm.iloc[:, col] = data.iloc[:, col] / denom

    for col in range(norm.shape[1]):
        norm.iloc[:, col] = norm.iloc[:, col] * weights[col]

    ideal_best = []
    ideal_worst = []

    for col in range(norm.shape[1]):
        if impacts[col] == "+":
            ideal_best.append(norm.iloc[:, col].max())
            ideal_worst.append(norm.iloc[:, col].min())
        else:
            ideal_best.append(norm.iloc[:, col].min())
            ideal_worst.append(norm.iloc[:, col].max())

    scores = []

    for i in range(norm.shape[0]):
        s_best = 0
        s_worst = 0
        for j in range(norm.shape[1]):
            s_best += (norm.iloc[i, j] - ideal_best[j]) ** 2
            s_worst += (norm.iloc[i, j] - ideal_worst[j]) ** 2
        s_best = s_best ** 0.5
        s_worst = s_worst ** 0.5
        scores.append(s_worst / (s_best + s_worst))

    df["Topsis Score"] = scores
    df["Rank"] = df["Topsis Score"].rank(ascending=False).astype(int)

    df.to_csv(output_file, index=False)
