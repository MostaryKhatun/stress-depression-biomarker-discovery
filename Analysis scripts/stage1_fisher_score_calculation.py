#TODO: Please Maintain the csv file names like this: "GSE22356_matrix_Transpose_labeled.csv"

import os
import numpy as np
import pandas as pd

# Define a function to calculate Fisher Score
def fisher_score(X, y):
    classes = np.unique(y)
    num_features = X.shape[1]
    scores = np.zeros(num_features)

    for i in range(num_features):
        feature = X.iloc[:, i]
        mean_total = np.mean(feature)
        numerator = 0
        denominator = 0
        
        for c in classes:
            class_data = feature[y == c]
            mean_class = np.mean(class_data)
            numerator += len(class_data) * (mean_class - mean_total) ** 2
            denominator += len(class_data) * np.var(class_data)
        
        scores[i] = numerator / (denominator + 1e-10)  # Add small constant to avoid division by zero

    return scores

# Input and output directories
input_directory = r"C:\Users\user\Documents\Schi_Work\datasets"  # Adjusted to the correct location for input datasets
output_root_directory = './Processed_Datasets'

# Create output subdirectories if they don't exist
score_dir = os.path.join(output_root_directory, 'Score')
os.makedirs(score_dir, exist_ok=True)

# Process each dataset file in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith('.csv'):
        dataset_path = os.path.join(input_directory, filename)
        dataset_name = os.path.splitext(filename)[0]  # Get the dataset name without extension
        
        try:
            # Load the dataset
            df = pd.read_csv(dataset_path)
        except Exception as e:
            print(f"Error reading file '{filename}': {e}. Skipping this file.")
            continue

        # Ensure the dataset has enough columns to separate features and target
        if df.shape[1] < 2:
            print(f"File '{filename}' does not have enough columns. Skipping this file.")
            continue

        try:
            # Assuming the last column is the target column
            X = df.iloc[:, :-1]  # All columns except the last one (features)
            y = df.iloc[:, -1]   # Last column (target)

            # Calculate Fisher Scores
            raw_scores = fisher_score(X, y)

            # Normalize the Fisher Scores to a range of 0 to 1
            min_score, max_score = np.min(raw_scores), np.max(raw_scores)
            normalized_scores = (raw_scores - min_score) / (max_score - min_score)

            # Create a DataFrame to hold features and their scores
            feature_scores = pd.DataFrame({
                'Feature': X.columns,
                'Fisher Score': raw_scores,
                'Normalized Fisher Score': normalized_scores,
            })

            # Save the Fisher scores with feature names to a CSV file in the Score directory
            feature_scores_output_file = os.path.join(score_dir, f'{dataset_name}_Fisher_Scores.csv')
            feature_scores.to_csv(feature_scores_output_file, index=False)
            print(f"Features and their Fisher Scores for '{dataset_name}' saved to '{feature_scores_output_file}'")
        
        except Exception as e:
            print(f"Error processing file '{filename}': {e}. Skipping this file.")

print("All datasets have been processed with Fisher scores.")