import requests
import os

# url = "https://shesharpnl.github.io/hackathon-2023.sourcestack-data/assets/junior-nl.csv"
url = "https://shesharpnl.github.io/hackathon-2023.sourcestack-data/assets/sourcestack-data-global.csv"

response = requests.get(url)
response.raise_for_status()

file_path = "./assets/sourcestack-data.csv"
os.makedirs(os.path.dirname(file_path), exist_ok=True)

with open(file_path, "wb") as file:
    file.write(response.content)
