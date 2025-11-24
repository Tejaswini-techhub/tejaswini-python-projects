import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DATA = 'movies_small.csv'

def create_sample():
    rows = [
        {'title':'Avengers','genre':'Action|Adventure','description':'Superheroes save the world.'},
        {'title':'Iron Man','genre':'Action|Sci-Fi','description':'A billionaire builds a suit of armor.'},
        {'title':'Thor','genre':'Action|Fantasy','description':'God of thunder fights enemies.'},
        {'title':'The Notebook','genre':'Romance|Drama','description':'A love story that spans years.'},
        {'title':'Interstellar','genre':'Sci-Fi|Drama','description':'Space travel to save humanity.'},
        {'title':'Captain America','genre':'Action|Adventure','description':'A soldier becomes a superhero.'},
    ]
    df = pd.DataFrame(rows)
    df.to_csv(DATA, index=False)

def recommend(title):
    if not pd.io.common.file_exists(DATA):
        create_sample()
    df = pd.read_csv(DATA)
    df['combined'] = df['genre'] + ' ' + df['description']
    cv = CountVectorizer(stop_words='english')
    mat = cv.fit_transform(df['combined'])
    sim = cosine_similarity(mat)
    if title not in df['title'].values:
        print('Title not in dataset. Available titles:')
        print(list(df['title']))
        return
    idx = df.index[df['title']==title][0]
    scores = list(enumerate(sim[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    # skip the first (itself)
    recs = [df['title'].iloc[i] for i,_ in scores[1:4]]
    print('Recommendations for', title, ':', recs)

def main():
    while True:
        cmd = input('Enter movie title to get recommendations (or "exit"): ').strip()
        if cmd.lower() == 'exit':
            break
        recommend(cmd)

if __name__ == '__main__':
    main()
