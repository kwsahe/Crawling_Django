import requests

apikey = "58df9d61"

url = f"https://www.omdbapi.com/?apikey={apikey}&i=imdbID"
response = requests.get(url)

print(response.text)