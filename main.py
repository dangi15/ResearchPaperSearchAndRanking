from tabulate import tabulate
import rec, pre, search, extraction

# Extraction
df = extraction.extract()

# Preprocessing
df = pre.preprocessing(df)

# Searching
searchType = input("(A)uthor/(R)easearch Paper: ").upper()
query = input("Enter your query: ").lower()
if searchType == 'A':
    result = search.authorSearch(query, df)
elif searchType == 'R':
    result = search.paperSearch(query, df)
else:
    print("Enter valid argument")

# Displaying
table_data = []
for i, row in result.iterrows():
    title = row.get('title', '')[:120]
    authors = row.get('authors', '')
    link = f"https://arxiv.org/abs/{row.get('id', '')}"
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
    title = df.iloc[int(i)].get('title', '')[:120]
    authors = df.iloc[int(i)].get('authors', '')
    link = f"https://arxiv.org/abs/{df.iloc[int(i)].get('id', '')}"
    rec_data.append([title, authors, link])
print('Similar Recommendations: ')
print(tabulate(rec_data, headers=headers, tablefmt='grid'))