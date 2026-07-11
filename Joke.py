import requests
import time

try:
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    status=response.status_code
    if status==200:
        print(f"Status : {status}")
        joke=response.json()
        print("=======Random Joke=======")
        print(f"{joke['setup']}")
        time.sleep(3)
        print(f"{joke['punchline']}")
    else:
        print("No joke loaded")
except requests.exceptions.RequestException as e:
    print("Failed to load the joke")
