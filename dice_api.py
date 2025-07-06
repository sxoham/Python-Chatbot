import requests

def roll_dice_api(num_dice=1, sides=6):
    url = f"https://rolz.org/api/?{num_dice}d{sides}.json"
    try:
        response = requests.get(url)
        data = response.json()

        return f"You rolled a {num_dice}d{sides}: {data['result']} {data['details']}"
    except Exception:
        return "Sorry, I couldn't roll the dice right now."
