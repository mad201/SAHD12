import requests

API_KEY = "your_youtube_safe_browsing_api_key"
BASE_URL = "https://safebrowsing.googleapis.com/v4/threatMatches:find"

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
        if "matches" in data and data["matches"]:
            return False  # If matches are found, it's not safe
        else:
            return True  # If no matches, it's safe
    else:
        print("Error:", response.status_code)
        return True

website_url = "https://www.youtube.com/channel/UCV1Ns3fF3unrbg9YPseAe2g"

if is_safe_to_visit(website_url):
    print("Website is safe to visit.")
else:
    print("Website may not be safe to visit.")
