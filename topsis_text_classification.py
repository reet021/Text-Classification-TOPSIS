import numpy as np
import pandas as pd

# Decision matrix
data = pd.DataFrame({
    'Accuracy': [0.88, 0.90, 0.86, 0.87, 0.89],
    'F1-score': [0.87, 0.89, 0.85, 0.86, 0.88],
    'Inference Time': [120, 140, 60, 80, 160],
    'Model Size': [420, 500, 250, 90, 480]
}, index=['BERT', 'RoBERTa', 'DistilBERT', 'ALBERT', 'XLNet'])

# Weights
weights = np.array([0.3, 0.3, 0.2, 0.2])

# Benefit (1) or Cost (0)
benefit = np.array([1, 1, 0, 0])

# Normalize the decision matrix
normalized = data / np.sqrt((data ** 2).sum())

# Weighted normalized matrix
weighted = normalized * weights

# Ideal best and worst
ideal_best = np.where(benefit == 1, weighted.max(), weighted.min())
ideal_worst = np.where(benefit == 1, weighted.min(), weighted.max())

# Distance calculation
distance_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
distance_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

# TOPSIS score
topsis_score = distance_worst / (distance_best + distance_worst)

# Ranking
data['TOPSIS Score'] = topsis_score
data['Rank'] = data['TOPSIS Score'].rank(ascending=False)

print(data.sort_values('Rank'))
