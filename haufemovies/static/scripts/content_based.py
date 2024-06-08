import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def movieRecommenderScript(movies):
    current_movie = {'title': 'The Lord of the Rings: The Return of the King', 'genre': 'Fantasy',
                     'description': 'The final confrontation between the forces of good and evil fighting for control of the future of Middle-earth. Frodo and Sam reach Mordor in their quest to destroy the One Ring, while Aragorn leads the forces of good against Sauron\'s evil army at the stone city of Minas Tirith.'}

    # def a TF-IDF Vectorizer
    tfidf = TfidfVectorizer(stop_words='english')

    tfidf_matrix = tfidf.fit_transform(movies['description'])
    tfidf_matrix.shape
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    def get_recommendations(title, amount=1, cosine_sim=cosine_sim, movies_df=movies):
        if title in movies_df['title'].values:
            idx = movies_df.loc[movies_df['title']
                                == title, 'id'].values[0]
        else:
            print(f"Book title '{title}' not found in the DataFrame.")
            return None
        sim_scores = list(enumerate(cosine_sim[idx]))

        # sort by most similar and get similar movie
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:amount+1]

        book_indices = [i[0] for i in sim_scores]

        recommended_movies = movies[[
            'title', 'genre', 'description']].iloc[book_indices]
        recommended_movies_df = pd.DataFrame(recommended_movies)
        return recommended_movies_df

    print(get_recommendations(current_movie['title'], amount=3))
    return
