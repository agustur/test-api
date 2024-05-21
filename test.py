import requests

url = "https://luisana-miamor-morales.onrender.com"

response = requests.get(url)
print(response.text)