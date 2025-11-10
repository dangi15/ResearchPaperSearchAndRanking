import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sentence_transformers import SentenceTransformer
import numpy as np
nltk.download('punkt_tab')
nltk.download('wordnet')

def preprocessing(df):
    df = df.dropna(subset=['title', 'abstract'])
    df = df.drop_duplicates(subset='id')

    df['text'] = df['title'].str.lower() + ' ' + df['abstract'].str.lower()
    df['clean_text'] = df['text'].apply(clean_text)

    model = SentenceTransformer('./all-MiniLM-L6-v2-local')
    embeddings = model.encode(df['clean_text'].astype(str).tolist(), show_progress_bar=False)
    np.save('D:/coding/Python/elective/sem3PBL/files/embeddings.npy', embeddings)
    df.to_csv('papers.csv', index=False)
    return df

def clean_text(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in stop_words]

    return ' '.join(tokens)