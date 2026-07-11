#!/usr/bin/env python3
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os

SCOPES = ["https://www.googleapis.com/auth/calendar"]
TOKEN_PATH = "/root/.hermes/google_token.json"
CLIENT_PATH = "/root/.hermes/google_client_secret.json"

def get_service():
    creds = None
    
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
    
    with open("google_token.json", "w") as f:
        f.write(creds.to_json())
    
    return build("calendar", "v3", credentials=creds)
