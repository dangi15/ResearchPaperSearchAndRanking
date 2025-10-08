import pandas as pd
import json
import zipfile

rows = []
with zipfile.ZipFile('D:/coding/Python/elective/archive.zip', 'r') as f:
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
print(df)