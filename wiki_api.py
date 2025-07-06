import requests

def get_wikipedia_summary(query):
    try:
        # First try direct summary lookup
        response = requests.get(
            f"https://en.wikipedia.org/api/rest_v1/page/summary/{query.replace(' ', '_')}"
        )

        # Handle successful lookup
        if response.status_code == 200:
            data = response.json()
            return f"{data['title']}:\n{data.get('extract', 'No summary available.')}"
        
        # If page exists but can't be summarized, fallback to search
        elif response.status_code == 404 or response.status_code == 500:
            # Try searching for better match
            search_response = requests.get(
                f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={query}&format=json"
            )
            results = search_response.json().get("query", {}).get("search", [])
            if results:
                # Try summary of top search result
                title = results[0]["title"]
                summary_response = requests.get(
                    f"https://en.wikipedia.org/api/rest_v1/page/summary/{title.replace(' ', '_')}"
                )
                if summary_response.status_code == 200:
                    summary_data = summary_response.json()
                    return f"{summary_data['title']}:\n{summary_data.get('extract', 'No summary available.')}"
                else:
                    return f"Could not fetch summary for '{title}'"
            else:
                return f"No Wikipedia results found for '{query}'."
        
        else:
            return f"Unexpected error: {response.status_code}"

    except Exception as e:
        return f"Something went wrong:\n{str(e)}"
