import requests
import json
import os

# Puoi specificare il linguaggio
LANGUAGE = os.getenv("LANGUAGE", "C++")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}
url = f"https://api.github.com/search/repositories?q=language:{LANGUAGE}&sort=stars&order=desc&per_page=100"

print(f"Fetching top 100 repositories for language: {LANGUAGE}")
response = requests.get(url, headers=headers)

if response.status_code != 200:
    raise Exception(f"GitHub API returned {response.status_code}: {response.text}")

data = response.json()
repos = [repo["full_name"] for repo in data["items"]]

# Salva l'elenco in un file per usarlo nel workflow
os.makedirs("output", exist_ok=True)
with open("output/top_repos.json", "w") as f:
    json.dump(repos, f, indent=2)

print(f"✅ Saved {len(repos)} repositories to output/top_repos.json")
