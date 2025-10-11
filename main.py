import pandas as pd
import json
import zipfile
from tabulate import tabulate

rows = []
filepath = 'C:/Users/Gaurav/OneDrive/Desktop/archive.zip'
with zipfile.ZipFile(filepath, 'r') as f:
    with f.open('arxiv-metadata-oai-snapshot.json') as f:
        for i, line in enumerate(f):
            if i >= 100000:
                break
            try:
                record = json.loads(line)
                record['id'] = str(record.get('id', ''))
                rows.append(record)
            except json.JSONDecodeError:
                continue

df = pd.DataFrame(rows)

def keywordSearch(query, df, limit=100):
    query = query.lower()
    results = df[df['title'].str.lower().str.contains(query, na=False) | df['abstract'].str.lower().str.contains(query, na=False)]
    return results.head(limit)

query = input("Enter your query: ")
result = keywordSearch(query, df)

table_data = []
for i, row in result.iterrows():
    title = row.get('title', '')[:120]
    authors = row.get('authors', '')
    link = f"https://arxiv.org/abs/{row.get('id', '')}"
    table_data.append([title, authors, link])

headers = ['Title', 'Authors', 'Link']
print(tabulate(table_data[0:10], headers=headers, tablefmt='grid'))
for i in range(10, 100, 10):
    c = input()
    if c=='e':
        print(tabulate(table_data[i:i+10], headers=headers, tablefmt='grid'))
    else:
        break