# movie_api.py
import requests

OMDB_API_KEY = "4b8cce33"  # Replace with your key

def get_movie_info(title):
    try:
        url = f"http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}"
        response = requests.get(url)
        data = response.json()

        if data["Response"] == "False":
            return f"Movie not found: {title}"

        return (f"🎬 Title: {data['Title']}\n"
                f"📅 Year: {data['Year']}\n"
                f"⭐ IMDB: {data['imdbRating']}\n"
                f"📝 Plot: {data['Plot']}\n"
                f"🎭 Genre: {data['Genre']}\n"
                f"🎬 Director: {data['Director']}")
    except Exception as e:
        return f"Error fetching movie info: {e}"