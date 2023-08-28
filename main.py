import requests
API_KEY = "youtube"
BASE_URL = "https://www.youtube.com/"


def is_safe_to_visit(url):
    payload = {
        "client": {
            "clientId": "Youtube",
            "clientVersion": "1.0.0"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(
        f"{BASE_URL}?key={API_KEY}",
        json=payload,
        headers=headers
    )

    if response.status_code == 200:
        data = response.json()
        if "matches" in data:
            return False
        else:
            return True
    else:
        print("Error:", response.status_code)
        return False


website_url = "https://www.youtube.com"

if is_safe_to_visit(website_url):
    print("Website is safe to visit.")
else:
    print("Website may not be safe to visit.")