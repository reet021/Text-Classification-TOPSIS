# Text Classification Model Selection using TOPSIS

Roll Number: 102303532

## Objective
The objective of this project is to identify the best pre-trained model for text classification using the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method.

## What is TOPSIS?
TOPSIS is a decision-making technique used to rank alternatives based on multiple criteria. The best option is the one closest to the ideal solution and farthest from the worst solution.

## Models Considered
The following pre-trained models were evaluated:
- BERT
- RoBERTa
- DistilBERT
- ALBERT
- XLNet

## Evaluation Criteria
The models were compared using the following criteria:
- Accuracy (Benefit)
- F1-score (Benefit)
- Inference Time in milliseconds (Cost)
- Model Size in MB (Cost)

## Methodology
1. A decision matrix was created using benchmark values.
2. The matrix was normalized.
3. Weights were assigned to each criterion.
4. Ideal best and ideal worst solutions were calculated.
5. TOPSIS scores were computed and models were ranked.

## Result
Based on the TOPSIS score, **RoBERTa-base** was identified as the best pre-trained model for text classification.

## Tools Used
- Python
- NumPy
- Pandas

## Conclusion
TOPSIS provides a systematic and mathematical approach to selecting the most suitable model by considering both performance and efficiency metrics.
