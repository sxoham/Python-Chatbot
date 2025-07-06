import requests

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any?safe-mode&type=single"  # Use "type=twopart" for 2-line jokes
    try:
        response = requests.get(url)
        data = response.json()

        if data["error"]:
            return "Oops! I couldn't fetch a joke right now."
        
        return data["joke"]
    except Exception:
        return "Sorry, joke service is currently unavailable."
