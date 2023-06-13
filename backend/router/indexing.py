from sentence_transformers import SentenceTransformer
import numpy as np
import json
import pandas as pd
from tqdm import tqdm
from sklearn.metrics.pairwise import cosine_similarity

import torch

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')



model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens')

df = pd.read_json('./startups_demo.json', lines=True)

# Here we ancode all startup descriptions
# We do encoding in batches, as this reduces overhead costs and significantly speeds up the process
vectors = []
batch_size = 64
batch = []
for row in tqdm(df.itertuples()):
  description = row.alt + ". " + row.description
  batch.append(description)
  if len(batch) >= batch_size:
    vectors.append(model.encode(batch))  # Text -> vector encoding happens here
    batch = []

if len(batch) > 0:
  vectors.append(model.encode(batch))
  batch = []

vectors = np.concatenate(vectors)
# print(vectors)

# print(vectors.shape)


# # Take a random description as a query
# sample_query = df.iloc[12345].description
# print(sample_query)


# query_vector = model.encode(sample_query)  # Convert query description into a vector.

# scores = cosine_similarity([query_vector], vectors)[0]  # Look for the most similar vectors, manually score all vectors
# top_scores_ids = np.argsort(scores)[-5:][::-1]  # Select top-5 with vectors the largest scores

# # Check if result similar to the query
# for top_id in top_scores_ids:
#   print(df.iloc[top_id].description)
#   print("-----")