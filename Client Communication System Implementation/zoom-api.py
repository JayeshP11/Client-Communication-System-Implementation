import os
import requests

# Create a new Zoom meeting
api_key = os.environ['ZOOM_API_KEY']
api_secret = os.environ['ZOOM_API_SECRET']
meeting_topic = "Client Meeting"
meeting_type = 2  # Scheduled meeting

response = requests.post(
    f"https://api.zoom.us/v2/meetings",
    headers={"Authorization": f"Bearer {api_key}"},
    json={"topic": meeting_topic, "type": meeting_type}
)
meeting_id = response.json()['id']

print(f"Meeting created: {meeting_id}")