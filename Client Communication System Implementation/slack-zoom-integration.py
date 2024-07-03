import os
import slack
import requests

# Integrate Slack and Zoom for seamless meeting scheduling and joining
slack_token = os.environ['SLACK_TOKEN']
zoom_api_key = os.environ['ZOOM_API_KEY']
zoom_api_secret = os.environ['ZOOM_API_SECRET']

# Create a new Slack app
app = slack.App(client_id=os.environ['SLACK_CLIENT_ID'], client_secret=os.environ['SLACK_CLIENT_SECRET'])

# Create a new Zoom meeting
meeting_topic = "Client Meeting"
meeting_type = 2  # Scheduled meeting

response = requests.post(
    f"https://api.zoom.us/v2/meetings",
    headers={"Authorization": f"Bearer {zoom_api_key}"},
    json={"topic": meeting_topic, "type": meeting_type}
)
meeting_id = response.json()['id']

# Create a new Slack message with Zoom meeting link
message = f"Join the meeting: https://zoom.us/j/{meeting_id}"
app.client.chat_postMessage(channel="#client-meeting", text=message)
print(f"Message sent: {message}")