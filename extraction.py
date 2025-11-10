import zipfile
import json
import pandas as pd

def extract():
    rows = []
    filepath = 'C:/Users/Gaurav/OneDrive/Desktop/archive.zip'
    with zipfile.ZipFile(filepath, 'r') as f:
        with f.open('arxiv-metadata-oai-snapshot.json') as f:
            for i, line in enumerate(f):
                if i >= 100000:
                    break
                try:
                    record = json.loads(line)
                    record_id = str(record.get('id', '')).strip()
                    rows.append({**record, 'id': record_id})
                except json.JSONDecodeError:
                    continue
    df = pd.DataFrame(rows, dtype='string')
    df['id'] = df['id'].astype(str)
    return df