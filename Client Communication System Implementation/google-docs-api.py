import os
import requests

# Create a new Google Doc
api_token = os.environ['GOOGLE_API_TOKEN']
doc_title = "Client Communication Document"
response = requests.post(
    f"https://docs.googleapis.com/v1/documents",
    headers={"Authorization": f"Bearer {api_token}"},
    json={"requests": [{"createDocument": {"documentId": doc_title}}]}
)
doc_id = response.json()['documentId']

print(f"Document created: {doc_id}")

# Create a new Google Doc section
section_title = "Client Communication Section"
response = requests.post(
    f"https://docs.googleapis.com/v1/documents/{doc_id}:batchUpdate",
    headers={"Authorization": f"Bearer {api_token}"},
    json={
        "requests": [
            {
                "insertText": {
                    "location": {"index": 0},
                    "text": section_title
                }
            }
        ]
    }
)

print(f"Section created: {section_title}")

# Create a new Google Doc paragraph
paragraph_text = "This is a sample paragraph for client communication."
response = requests.post(
    f"https://docs.googleapis.com/v1/documents/{doc_id}:batchUpdate",
    headers={"Authorization": f"Bearer {api_token}"},
    json={
        "requests": [
            {
                "insertText": {
                    "location": {"index": 1},
                    "text": paragraph_text
                }
            }
        ]
    }
)

print(f"Paragraph created: {paragraph_text}")

# Integrate Google Docs with Jira and GitHub
def update_google_doc(issue_id, issue_title, issue_body):
    # Get the Google Doc ID
    doc_id = os.environ['GOOGLE_DOC_ID']

    # Update the Google Doc with the issue details
    response = requests.post(
        f"https://docs.googleapis.com/v1/documents/{doc_id}:batchUpdate",
        headers={"Authorization": f"Bearer {api_token}"},
        json={
            "requests": [
                {
                    "insertText": {
                        "location": {"index": 2},
                        "text": f"Issue {issue_id}: {issue_title}\n{issue_body}"
                    }
                }
            ]
        }
    )

    print(f"Google Doc updated: {doc_id}")

# Call the update_google_doc function when a Jira issue is updated
def jira_issue_updated(event):
    issue_id = event['issue']['id']
    issue_title = event['issue']['fields']['summary']
    issue_body = event['issue']['fields']['description']
    update_google_doc(issue_id, issue_title, issue_body)

# Call the update_google_doc function when a GitHub issue is updated
def github_issue_updated(event):
    issue_id = event['issue']['id']
    issue_title = event['issue']['title']
    issue_body = event['issue']['body']
    update_google_doc(issue_id, issue_title, issue_body)

print("Google Docs integration complete!")