import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

data = {
    'movie_id': [1, 2, 3, 4, 5],
    'title': ['The Matrix', 'John Wick', 'The Notebook', 'La La Land', 'Avengers'],
    'genres': ['Action Sci-Fi', 'Action Thriller', 'Romance Drama', 'Romance Musical', 'Action Sci-Fi']
}
df = pd.DataFrame(data)
vectorizer = CountVectorizer()
genre_matrix = vectorizer.fit_transform(df['genres'])
similarity = cosine_similarity(genre_matrix)

def recommend(movie_title, df, similarity):
    if movie_title not in df['title'].values:
        return []
    idx = df[df['title'] == movie_title].index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    recommendations = [df.iloc[i[0]]['title'] for i in scores[1:4]]
    return recommendations

ratings = {
    'user_id': [1, 1, 1, 2, 2, 3, 3],
    'movie': ['The Matrix', 'John Wick', 'Avengers', 'The Notebook', 'La La Land', 'John Wick', 'Avengers'],
    'rating': [5, 4, 5, 5, 4, 4, 5]
}
df_ratings = pd.DataFrame(ratings)
user_movie_matrix = df_ratings.pivot_table(index='user_id', columns='movie', values='rating').fillna(0)
similarity_cf = cosine_similarity(user_movie_matrix.T)
similarity_df = pd.DataFrame(similarity_cf, index=user_movie_matrix.columns, columns=user_movie_matrix.columns)

def recommend_movie(movie_name, similarity_df):
    if movie_name not in similarity_df.columns:
        return []
    similar_movies = similarity_df[movie_name].sort_values(ascending=False)[1:4]
    return list(similar_movies.index)

print("Content-based:", recommend('The Matrix', df, similarity))
print("Collaborative filtering:", recommend_movie('John Wick', similarity_df))
