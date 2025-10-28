from sentence_transformers import SentenceTransformer, util

def recommendations(query, df):
    model = SentenceTransformer('all-MiniLM-L6-v2')

    results = df['clean_text']

    query = model.encode(query)

    index = []
    x = 0
    count = 0
    for i in results:
        if(count>=5):
            break
        abstract = model.encode(i)
        similarity = util.cos_sim(query, abstract)[0]
        if(float(similarity)>0.2):
            count += 1
            index.append(x)
        x += 1

    return index