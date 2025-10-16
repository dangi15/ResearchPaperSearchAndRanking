import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt_tab')
nltk.download('wordnet')

def preprocessing(df):
    df = df.dropna(subset=['title', 'abstract'])
    df = df.drop_duplicates(subset='id')

    df['text'] = df['title'].str.lower() + ' ' + df['abstract'].str.lower()

    df['clean_text'] = df['text'].apply(clean_text)
    return df

def clean_text(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t.isalpha() and t not in stop_words]

    return ' '.join(tokens)