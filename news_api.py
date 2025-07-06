import requests

def get_news(query=None):
    try:
        base_url = "https://gnews.io/api/v4/search"
        api_key = "c1ea2d944c2373a21c6a67a599db28a8"

        params = {
            "token": api_key,
            "lang": "en",
            "max": 5,
        }

        if query:
            params["q"] = query

        response = requests.get(base_url, params=params)
        print("DEBUG: status =", response.status_code)
        print("DEBUG: response =", response.text)

        data = response.json()

        if "articles" not in data or not data["articles"]:
            return " No articles found. Try a different query or check your API plan."

        headlines = [f" {article['title']}" for article in data["articles"]]
        return "\n\n".join(headlines)

    except Exception as e:
        return f" Failed to fetch news:\n{str(e)}"