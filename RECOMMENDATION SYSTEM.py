# Sample movie dataset with genres
movies = {
     "MAX": ["Action"],
    "SPIDER MAN": ["Action"],
    "ROBERT": ["Action"],
    "ITS END WITH US": ["Romance", "Drama"],
    "DIL BECHARA": ["Romance", "Drama"],
    "LOVE MOCKTAIL": ["Romance"],
    "TAMASHA": ["Romance","DRAMA"],
    "BRAMASTRA": ["Sci-fi", "Action"],
    "BLINK": ["Sci-fi","Mythological"],
    "RAVAN":["sci-fi","Action"],
    "KANTARA":["Action","Adventure","Drama"],
    "CHOO MANTHAR":["Horror","Thriller"],
    "LAST BUS":["Horror","Fantasy","Thriller"],
    "BHOO KAILASA":["Mythological"],
    "BHAJARANGI":["Mythological","Adventure","Fantasy"],
    "CHARLIE 777": ["DRAMA"],
}

# Function to get movie recommendations based on a preferred genre
def recommend_movies(favorite_movie):
    if favorite_movie not in movies:
        print("Sorry, movie not found in our database.")
        return []

    favorite_genres = movies[favorite_movie]
    recommendations = []

    for movie, genres in movies.items():
        if movie != favorite_movie and any(genre in favorite_genres for genre in genres):
            recommendations.append(movie)

    return recommendations

# Example usage
user_movie = input("Enter a movie you like: ")
recommendations = recommend_movies(user_movie)

if recommendations:
    print("You might also like:", ", ".join(recommendations))
else:
    print("No recommendations found.")

