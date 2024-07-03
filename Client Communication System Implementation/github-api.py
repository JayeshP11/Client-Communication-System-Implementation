import os
import requests

# Create a new GitHub repository
api_token = os.environ['GITHUB_API_TOKEN']
repo_name = "Client Communication"
response = requests.post(
    f"https://api.github.com/repos/{repo_name}",
    headers={"Authorization": f"Bearer {api_token}"},
    json={"name": repo_name}
)
repo_id = response.json()['id']

print(f"Repository created: {repo_id}")

# Create a new GitHub issue
issue_title = "Client Communication Issue"
response = requests.post(
    f"https://api.github.com/repos/{repo_name}/issues",
    headers={"Authorization": f"Bearer {api_token}"},
    json={"title": issue_title}
)
issue_id = response.json()['id']

print(f"Issue created: {issue_id}")