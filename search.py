from rapidfuzz import fuzz

def paperSearch(query, df, limit=100):
    scores = []

    for i, row in df.iterrows():
        text = row.get('clean_text', '')
        score = fuzz.partial_ratio(query, text)
        if score >= 70:
            scores.append((i, score))
    
    scores.sort(key=lambda x: x[1], reverse=True)

    top_indices = [i for i in scores[:limit]]
    return top_indices

def authorSearch(query, df, limit=100):
    results = df[df['authors'].str.contains(query, na=False)]
    return results.head(limit)