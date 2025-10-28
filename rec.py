from sentence_transformers import SentenceTransformer, util
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = np.load('D:/coding/Python/elective/sem3PBL/files/embeddings.npy')

def recommendations(query, df):
    query_emb = model.encode(query, convert_to_tensor=True)
    corpus_emb = embeddings

    cosine_scores = util.cos_sim(query_emb, corpus_emb)[0]
    indices = np.argsort(-cosine_scores)[:5].tolist()

    return indices