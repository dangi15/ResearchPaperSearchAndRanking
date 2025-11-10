from sentence_transformers import SentenceTransformer, util
import numpy as np
import torch
import os

model = SentenceTransformer('./all-MiniLM-L6-v2-local')
embeddings_path = 'files/embeddings.npy'
if os.path.exists(embeddings_path):
    embeddings = np.load(embeddings_path)
else:
    raise FileNotFoundError("Embeddings file not found. Run preprocessing first.")

def semanticSearch(query, df, top_k=50):
    query_emb = model.encode(query, convert_to_tensor=True)

    corpus_emb = torch.tensor(embeddings)

    cosine_scores = util.cos_sim(query_emb, corpus_emb)[0]

    top_indices = torch.topk(cosine_scores, k=top_k).indices.tolist()

    return top_indices
