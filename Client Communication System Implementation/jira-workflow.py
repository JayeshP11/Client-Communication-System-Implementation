import os
import requests

# Configure Jira workflows and issue tracking
api_key = os.environ['JIRA_API_KEY']
api_secret = os.environ['JIRA_API_SECRET']
instance_name = "Client Communication"

# Create a new Jira workflow
workflow_name = "Client Communication Workflow"
response = requests.post(
    f"https://api.atlassian.com/jira/{instance_name}/rest/api/2/workflow",
    headers={"Authorization": f"Bearer {api_key}"},
    json={"name": workflow_name}
)
workflow_id = response.json()['id']

print(f"Workflow created: {workflow_id}")

# Configure Jira workflow transitions
transitions = [
    {"name": "Open", "from": "Open", "to": "In Progress"},
    {"name": "In Progress", "from": "In Progress", "to": "Done"},
    {"name": "Done", "from": "Done", "to": "Closed"}
]

for transition in transitions:
    response = requests.post(
        f"https://api.atlassian.com/jira/{instance_name}/rest/api/2/workflow/{workflow_id}/transition",
        headers={"Authorization": f"Bearer {api_key}"},
        json=transition
    )
    print(f"Transition created: {transition['name']}")

# Configure Jira workflow statuses
statuses = [
    {"name": "Open", "description": "Issue is open"},
    {"name": "In Progress", "description": "Issue is in progress"},
    {"name": "Done", "description": "Issue is done"},
    {"name": "Closed", "description": "Issue is closed"}
]

for status in statuses:
    response = requests.post(
        f"https://api.atlassian.com/jira/{instance_name}/rest/api/2/workflow/{workflow_id}/status",
        headers={"Authorization": f"Bearer {api_key}"},
        json=status
    )
    print(f"Status created: {status['name']}")

# Associate Jira workflow with project
project_id = "Client Communication"
response = requests.put(
    f"https://api.atlassian.com/jira/{instance_name}/rest/api/2/project/{project_id}/workflow",
    headers={"Authorization": f"Bearer {api_key}"},
    json={"workflowId": workflow_id}
)
print(f"Workflow associated with project: {project_id}")