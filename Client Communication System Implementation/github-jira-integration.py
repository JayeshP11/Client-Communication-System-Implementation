import os
import requests

# Configure GitHub and Jira integration
github_api_token = os.environ['GITHUB_API_TOKEN']
jira_api_key = os.environ['JIRA_API_KEY']
jira_api_secret = os.environ['JIRA_API_SECRET']
instance_name = "Client Communication"

# Create a new GitHub webhook
repo_name = "Client Communication"
webhook_url = f"https://api.github.com/repos/{repo_name}/hooks"
response = requests.post(
    webhook_url,
    headers={"Authorization": f"Bearer {github_api_token}"},
    json={
        "name": "web",
        "active": True,
        "events": ["issues"],
        "config": {
            "url": "https://example.com/jira-webhook",
            "content_type": "json"
        }
    }
)
webhook_id = response.json()['id']

print(f"Webhook created: {webhook_id}")

# Create a new Jira webhook
jira_webhook_url = f"https://api.atlassian.com/jira/{instance_name}/rest/api/2/webhook"
response = requests.post(
    jira_webhook_url,
    headers={"Authorization": f"Bearer {jira_api_key}"},
    json={
        "name": "GitHub Webhook",
        "url": "https://example.com/github-webhook",
        "events": ["jira:issue_updated"]
    }
)
jira_webhook_id = response.json()['id']

print(f"Jira webhook created: {jira_webhook_id}")

# Configure GitHub and Jira integration
def github_issue_updated(event):
    # Get the GitHub issue details
    issue_id = event['issue']['id']
    issue_title = event['issue']['title']
    issue_body = event['issue']['body']

    # Create a new Jira issue
    jira_issue_url = f"https://api.atlassian.com/jira/{instance_name}/rest/api/2/issue"
    response = requests.post(
        jira_issue_url,
        headers={"Authorization": f"Bearer {jira_api_key}"},
        json={
            "fields": {
                "summary": issue_title,
                "description": issue_body,
                "project": {"key": "Client Communication"},
                "issuetype": {"name": "Task"}
            }
        }
    )
    jira_issue_id = response.json()['id']

    print(f"Jira issue created: {jira_issue_id}")

    # Update the GitHub issue with the Jira issue ID
    github_issue_url = f"https://api.github.com/repos/{repo_name}/issues/{issue_id}"
    response = requests.patch(
        github_issue_url,
        headers={"Authorization": f"Bearer {github_api_token}"},
        json={"body": f"Jira issue: {jira_issue_id}"}
    )

    print(f"GitHub issue updated: {issue_id}")

def jira_issue_updated(event):
    # Get the Jira issue details
    issue_id = event['issue']['id']
    issue_title = event['issue']['fields']['summary']
    issue_body = event['issue']['fields']['description']

    # Update the corresponding GitHub issue
    github_issue_url = f"https://api.github.com/repos/{repo_name}/issues/{issue_id}"
    response = requests.patch(
        github_issue_url,
        headers={"Authorization": f"Bearer {github_api_token}"},
        json={"title": issue_title, "body": issue_body}
    )

    print(f"GitHub issue updated: {issue_id}")

# Start the webhook listener
print("Webhook listener started...")