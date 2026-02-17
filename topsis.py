import sys
import pandas as pd
import numpy as np

args = sys.argv

if len(args) != 5:
    print("Wrong number of arguments")
    sys.exit()

input_file = args[1]
weights_input = args[2]
impacts_input = args[3]
output_file = args[4]

try:
    df = pd.read_csv(input_file)
except:
    print("File not found")
    sys.exit()

columns_count = df.shape[1]

if columns_count < 3:
    print("File must have at least 3 columns")
    sys.exit()

numeric_data = df.iloc[:, 1:]

try:
    numeric_data = numeric_data.astype(float)
except:
    print("All columns except first must be numeric")
    sys.exit()

weights_list = weights_input.split(",")
impacts_list = impacts_input.split(",")

if len(weights_list) != numeric_data.shape[1]:
    print("Weights count mismatch")
    sys.exit()

if len(impacts_list) != numeric_data.shape[1]:
    print("Impacts count mismatch")
    sys.exit()

for item in impacts_list:
    if item != "+" and item != "-":
        print("Impacts must be + or - only")
        sys.exit()

weights = []
for w in weights_list:
    weights.append(float(w))

weights = np.array(weights)

normalized = numeric_data.copy()

for col in range(numeric_data.shape[1]):
    column_values = numeric_data.iloc[:, col]
    denominator = 0
    for val in column_values:
        denominator = denominator + val * val
    denominator = denominator ** 0.5
    normalized.iloc[:, col] = column_values / denominator

weighted = normalized.copy()

for col in range(weighted.shape[1]):
    weighted.iloc[:, col] = weighted.iloc[:, col] * weights[col]

ideal_best = []
ideal_worst = []

for col in range(weighted.shape[1]):
    column_values = weighted.iloc[:, col]
    if impacts_list[col] == "+":
        ideal_best.append(max(column_values))
        ideal_worst.append(min(column_values))
    else:
        ideal_best.append(min(column_values))
        ideal_worst.append(max(column_values))

dist_best = []
dist_worst = []

for i in range(weighted.shape[0]):
    row = weighted.iloc[i]
    sum_best = 0
    sum_worst = 0
    for j in range(len(row)):
        sum_best = sum_best + (row.iloc[j] - ideal_best[j]) ** 2
        sum_worst = sum_worst + (row.iloc[j] - ideal_worst[j]) ** 2
    dist_best.append(sum_best ** 0.5)
    dist_worst.append(sum_worst ** 0.5)

scores = []

for i in range(len(dist_best)):
    score = dist_worst[i] / (dist_best[i] + dist_worst[i])
    scores.append(score)

df["Topsis Score"] = scores

ranks = df["Topsis Score"].rank(ascending=False)
df["Rank"] = ranks.astype(int)

df.to_csv(output_file, index=False)

print("Done. Output saved.")
