from tabulate import tabulate
import rec, pre, search, extraction
import pandas as pd
import os

if os.path.exists('D:/coding/Python/elective/sem3PBL/files/papers.csv'):
    df = pd.read_csv('D:/coding/Python/elective/sem3PBL/files/papers.csv')
else:
    # Extraction
    df = extraction.extract()
    # Preprocessing
    df = pre.preprocessing(df)


# Searching
searchType = input("(A)uthor/(R)esearch Paper: ").upper()
while True:
    if searchType=='A' or searchType=='R':
        break
    print("Enter valid argument")
    searchType = input("(A)uthor/(R)esearch Paper: ").upper()
query = input("Enter your query: ").lower()
if searchType == 'A':
    result = search.authorSearch(query, df)
elif searchType == 'R':
    result = search.paperSearch(query, df)

# Displaying
table_data = []
for i in result:
    title = df.iloc[i[0]].get('title', '')[:120]
    authors = df.iloc[i[0]].get('authors', '')
    link = f"https://arxiv.org/abs/{df.iloc[i[0]].get('id', '')}"
    table_data.append([title, authors, link])

headers = ['Title', 'Authors', 'Link']
print(tabulate(table_data[0:10], headers=headers, tablefmt='grid'))

for i in range(10, len(table_data), 10):
    c = input("(N)ext/(E)xit: ").lower()
    if c=='n':
        print(tabulate(table_data[i:i+10], headers=headers, tablefmt='grid'))
    else:
        break

rec_data = []
index = rec.recommendations(query, df)
for i in index:
    title = df.iloc[i].get('title', '')[:120]
    authors = df.iloc[i].get('authors', '')
    link = f"https://arxiv.org/abs/{df.iloc[i].get('id', '')}"
    rec_data.append([title, authors, link])
print('Similar papers you might like: ')
print(tabulate(rec_data, headers=headers, tablefmt='grid'))