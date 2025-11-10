from sentence_transformers import SentenceTransformer, util
import numpy as np
import torch
import os

model = SentenceTransformer('./all-MiniLM-L6-v2-local')

embeddings_path =r'C:\Users\saksh\OneDrive\Desktop\python\files\embeddings.npy'

if os.path.exists(embeddings_path):
    embeddings = np.load(embeddings_path)
else:
    raise FileNotFoundError("Embeddings file not found. Run preprocessing first.")

def recommendations(search_results_df, top_k=5):
    excluded_ids = search_results_df

    # indices = search_results_df.index.tolist()
    selected_embeddings = torch.tensor(embeddings[search_results_df])

    mean_emb = selected_embeddings.mean(dim=0, keepdim=True)

    corpus_emb = torch.tensor(embeddings)
    cosine_scores = util.cos_sim(mean_emb, corpus_emb)[0]

    sorted_indices = torch.argsort(cosine_scores, descending=True).tolist()
    recommended_indices = [idx for idx in sorted_indices if idx not in excluded_ids][:top_k]
    print(recommended_indices)
    return recommended_indices
