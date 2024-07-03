import os
import requests

# Test Jira workflow
response = requests.post(
    f"https://api.atlassian.com/jira/{instance_name}/rest/api/2/workflow",
    headers={"Authorization": f"Bearer {api_key}"},
    json={"name": "Test Workflow"}
)
print(response.json())

# Test GitHub API
response = requests.post(
    f"https://api.github.com/repos/{repo_name}/issues",
    headers={"Authorization": f"Bearer {github_api_token}"},
    json={"title": "Test Issue", "body": "This is a test issue"}
)
print(response.json())

# Test Google Docs API
response = requests.post(
    f"https://docs.googleapis.com/v1/documents",
    headers={"Authorization": f"Bearer {api_token}"},
    json={"requests": [{"createDocument": {"documentId": "Test Document"}}]}
)
print(response.json())

# Test Jira-GitHub integration
jira_issue_id = 123
github_issue_id = 456
response = requests.post(
    f"https://api.atlassian.com/jira/{instance_name}/rest/api/2/issue/{jira_issue_id}",
    headers={"Authorization": f"Bearer {api_key}"},
    json={"fields": {"summary": "Test Issue", "description": "This is a test issue"}}
)
print(response.json())

response = requests.post(
    f"https://api.github.com/repos/{repo_name}/issues/{github_issue_id}",
    headers={"Authorization": f"Bearer {github_api_token}"},
    json={"title": "Test Issue", "body": "This is a test issue"}
)
print(response.json())

# Test GitHub-Jira integration
github_issue_id = 456
jira_issue_id = 123
response = requests.post(
    f"https://api.github.com/repos/{repo_name}/issues/{github_issue_id}",
    headers={"Authorization": f"Bearer {github_api_token}"},
    json={"title": "Test Issue", "body": "This is a test issue"}
)
print(response.json())

response = requests.post(
    f"https://api.atlassian.com/jira/{instance_name}/rest/api/2/issue/{jira_issue_id}",
    headers={"Authorization": f"Bearer {api_key}"},
    json={"fields": {"summary": "Test Issue", "description": "This is a test issue"}}
)
print(response.json())

# Test Google Docs-Jira integration
google_doc_id = "Test Document"
jira_issue_id = 123
response = requests.post(
    f"https://docs.googleapis.com/v1/documents/{google_doc_id}:batchUpdate",
    headers={"Authorization": f"Bearer {api_token}"},
    json={"requests": [{"insertText": {"location": {"index": 0}, "text": "Test Document"}}]}
)
print(response.json())

response = requests.post(
    f"https://api.atlassian.com/jira/{instance_name}/rest/api/2/issue/{jira_issue_id}",
    headers={"Authorization": f"Bearer {api_key}"},
    json={"fields": {"summary": "Test Issue", "description": "This is a test issue"}}
)
print(response.json())

print("Testing complete!")