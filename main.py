import pandas as pd
import json
import zipfile
from tabulate import tabulate
import rec

rows = []
filepath = 'C:/Users/ragha/Downloads/archive.zip'
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

def authorSearch(query, df, limit=100):
    query = query.lower()
    results = df[df['authors'].str.lower().str.contains(query, na=False)]
    return results.head(limit)

searchType = input("(A)uthor/(R)easearch Paper: ").upper()
query = input("Enter your query: ")
if searchType=='A':
    result = authorSearch(query, df)
elif searchType=='R':
    result = keywordSearch(query, df)
else:
    print("Enter valid argument")

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
    if c=='n':
        print(tabulate(table_data[i:i+10], headers=headers, tablefmt='grid'))
    else:
        break

rec_data = []
index = rec.recommendations(query, df)
for i in index:
    title = df.iloc[int(i)].get('title', '')[:120]
    authors = df.iloc[int(i)].get('authors', '')
    link = f"https://arxiv.org/abs/{df.iloc[int(i)].get('id', '')}"
    rec_data.append([title, authors, link])
print(tabulate(rec_data, headers=headers, tablefmt='grid'))