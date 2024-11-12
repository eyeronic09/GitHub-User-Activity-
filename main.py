import requests
def activity(username):
    pass


url = "https://api.github.com/users/kamranahmedse/events"

response  = requests.get(url)
if response.status_code == 200:
    # Convert response to JSON
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")