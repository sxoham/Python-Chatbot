import requests

def convert_currency(amount, from_currency, to_currency):
    try:
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        url = "https://api.exchangerate.host/convert"

        params = {
            "from": from_currency,
            "to": to_currency,
            "amount": amount,
            "access_key": "6ef7706505f20d778c89a19b6c8f5959"  # ✅ Your access key
        }

        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code != 200:
            return f"❌ API error: {response.status_code}"

        result = data.get("result")
        if result is None:
            return f"❌ No result for {amount} {from_currency} to {to_currency}."

        return f"{amount} {from_currency} = {result:.2f} {to_currency}"
    except Exception as e:
        return f"⚠️ Currency conversion failed:\n{str(e)}"
