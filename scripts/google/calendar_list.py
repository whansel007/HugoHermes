from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import os

SCOPES = ["https://www.googleapis.com/auth/calendar"]

def get_service():
    creds = None
    
    if os.path.exists("google_token.json"):
        creds = Credentials.from_authorized_user_file("google_token.json", SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("google_client_secret.json", SCOPES)
            creds = flow.run_local_server(port=0)
    
    with open("google_token.json", "w") as f:
        f.write(creds.to_json())
    
    return build("calendar", "v3", credentials=creds)

def list_events(max_results=10):
    service = get_service()
    
    now_raw = datetime.now() 
    now = now_raw.strftime('%Y-%m-%dT%H:%M:%S+08:00')
    
    response = service.events().list(
        calendarId="primary",
        maxResults=max_results,
        singleEvents=True,
        orderBy="startTime",
        timeMin=now,
    ).execute()
    
    events = response.get("items", [])
    
    for e in events:
        title = e.get("summary", "(u forgot to title this one >_>)")
        start = e["start"].get("dateTime", e["start"].get("date"))
        print(f"{start} - {title}")
        
list_events()