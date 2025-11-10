from flask import Flask, render_template, request
import pandas as pd
import pre, extraction, search, rec
import os

app = Flask(__name__)

if os.path.exists('files/papers.csv'):
    df = pd.read_csv('files/papers.csv', dtype={'id': str})
else:
    df = extraction.extract()
    df = pre.preprocessing(df)


@app.route('/')
def home():
    return render_template('index.html', search_results=[], recommendations=[], query=None)


@app.route('/search', methods=['POST'])
def handle_search():
    query = request.form.get('query', '').lower()

    search_results_df = search.semanticSearch(query, df)

    search_list = []
    for i in search_results_df:
        search_list.append({
            'title': df.iloc[i].get('title', '')[:120],
            'authors': df.iloc[i].get('authors', '')[:120],
            'link': f"https://arxiv.org/abs/{df.iloc[i].get('id', '')}"
        })

    rec_index = rec.recommendations(search_results_df)
    rec_list = []
    for i in rec_index:
        rec_list.append({
            'title': df.iloc[i].get('title', '')[:120],
            'authors': df.iloc[i].get('authors', ''),
            'link': f"https://arxiv.org/abs/{df.iloc[i].get('id', '')}"
        })

    return render_template('index.html',
                           search_results=search_list,
                           recommendations=rec_list,
                           query=query)

if __name__ == '__main__':
    app.run(debug=True)