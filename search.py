def paperSearch(query, df, limit=100):
    results = df[df['clean_text'].str.contains(query, na=False)]
    return results.head(limit)

def authorSearch(query, df, limit=100):
    results = df[df['authors'].str.contains(query, na=False)]
    return results.head(limit)