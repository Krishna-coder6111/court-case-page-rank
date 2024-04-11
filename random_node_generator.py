import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv('google_scholar_case_law_results.csv')
data.fillna('0', inplace=True)
data = data[:500]
# Get the number of cases
n = len(data)

# Initialize an n x n adjacency matrix
adj_matrix = np.zeros((n, n), dtype=int)

# Seed for reproducibility
np.random.seed(42)

# Populate the adjacency matrix
for index, row in data.iterrows():
    if pd.notna(row['cited_by_count']) and row['cited_by_count'] > 0:
        possible_indices = list(range(n))
        possible_indices.remove(index)  # A case cannot cite itself
        
        # Randomly choose cases to be cited by the current case
        # size = min(int(row['cited_by_count']), n)
        cited_cases = np.random.choice(possible_indices, int(row['cited_by_count']), replace=True)
        
        # Set the corresponding entries in the matrix to 1
        for cited_case in cited_cases:
            adj_matrix[cited_case][index] = 1  # cited_case is cited by the current case (index)

# Convert the adjacency matrix into a DataFrame for easier manipulation and viewing
adj_matrix_df = pd.DataFrame(adj_matrix, index=data['result_id'], columns=data['result_id'])

# Print the adjacency matrix DataFrame
print(adj_matrix_df)

# Save the adjacency matrix DataFrame to a CSV file
adj_matrix_df.to_csv('adjacency_matrix.csv')

#separate the data into source target and weight
source = []
target = []
weight = []

for i in range(adj_matrix.shape[0]):
    for j in range(adj_matrix.shape[1]):
        if adj_matrix[i, j] == 1 and i != j:
            source.append(adj_matrix_df.index[i]) 
            target.append(adj_matrix_df.index[j])  
            weight.append(1)

citations_df = pd.DataFrame({'source': source, 'target': target, 'weight': weight})
citations_df.to_csv('citations.csv')
print(citations_df)

#1000 citations = 637000 rows of connections - more than 30 mins maybe
#200 citations = 39266 rows 2mins to run