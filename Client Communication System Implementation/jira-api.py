import os
import requests

# Create a new Jira instance
api_key = os.environ['JIRA_API_KEY']
api_secret = os.environ['JIRA_API_SECRET']
instance_name = "Client Communication"

response = requests.post(
    f"https://api.atlassian.com/jira/{instance_name}/rest/api/2/instance",
    headers={"Authorization": f"Bearer {api_key}"},
    json={"name": instance_name}
)
print(f"Instance created: {response.json()['id']}")

# Set up Jira project and issue tracking
project_name = "Client Communication"
response = requests.post(
    f"https://api.atlassian.com/jira/{instance_name}/rest/api/2/project",
    headers={"Authorization": f"Bearer {api_key}"},
    json={"name": project_name}
)
project_id = response.json()['id']

issue_type_name = "Client Communication"
response = requests.post(
    f"https://api.atlassian.com/jira/{instance_name}/rest/api/2/issuetype",
    headers={"Authorization": f"Bearer {api_key}"},
    json={"name": issue_type_name}
)
issue_type_id = response.json()['id']