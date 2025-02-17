import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Sample dataset (movies with genres)
data = {
    'MovieID': [1, 2, 3, 4, 5],
    'Title': ['The Matrix', 'Inception', 'Interstellar', 'The Dark Knight', 'Memento'],
    'Genre': ['Action Sci-Fi', 'Sci-Fi Thriller', 'Sci-Fi Drama', 'Action Thriller', 'Mystery Thriller']
}

movies = pd.DataFrame(data)

# Content-based filtering using genres
def recommend_movies(movie_title, movies_df, top_n=3):
    # Create a count matrix from the 'Genre' column
    count_vectorizer = CountVectorizer()
    count_matrix = count_vectorizer.fit_transform(movies_df['Genre'])

    # Compute cosine similarity between movies
    cosine_sim = cosine_similarity(count_matrix, count_matrix)

    # Create a mapping of movie titles to indices
    movie_indices = pd.Series(movies_df.index, index=movies_df['Title']).drop_duplicates()

    # Get the index of the movie
    idx = movie_indices[movie_title]

    # Get similarity scores for all movies with the input movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort movies by similarity score
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the top N most similar movies
    top_movies = sim_scores[1:top_n+1]

    # Get the movie titles
    recommended_movies = [movies_df['Title'].iloc[i[0]] for i in top_movies]

    return recommended_movies

# Example usage
movie_to_recommend = 'Inception'
recommendations = recommend_movies(movie_to_recommend, movies)
print(f"Movies recommended for '{movie_to_recommend}': {recommendations}")
