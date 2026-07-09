#!/usr/bin/env python3
"""
Bare-bones Google Calendar script — ANNOTATED for learning.

WHAT THIS SCRIPT DOES
----------------------
Talks to Google's Calendar API to (1) list your upcoming events and
(2) create a new event. Everything else (auth, tokens) is plumbing
needed to be *allowed* to make those two calls.

SETUP (one-time):
  pip install google-auth-oauthlib google-api-python-client

  1. Go to https://console.cloud.google.com/ and enable the
     "Google Calendar API" for a project.
  2. Create OAuth credentials (type: "Desktop app") and download the
     JSON file. Save it as credentials.json next to this script.
     This file identifies *your app* to Google (not you personally).

Run:
  python calendar_simple.py
"""

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os

# SCOPES = what permissions we're asking the user to grant.
# "calendar" (full access) lets us both read and write events.
# If you only ever wanted to read, you could use the narrower
# "calendar.readonly" scope instead — good practice to ask for
# the minimum you need.
SCOPES = ["https://www.googleapis.com/auth/calendar"]


def get_service():
    """
    Handles authentication and returns a 'service' object — this is
    the client you call API methods on (like service.events()...).

    The flow:
      1. If we already logged in before, a token.json file exists.
         Load it instead of asking the user to log in again.
      2. If there's no token, or the token expired and can't be
         silently refreshed, launch the OAuth browser flow so the
         user logs in and grants permission.
      3. Save whatever valid token we end up with, so next time we
         skip straight to step 1.
    """
    creds = None

    # Step 1: reuse a saved login if we have one.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # Step 2: if there's no token, or it's invalid/expired...
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            # Access tokens expire (usually after 1 hour), but the
            # refresh_token lets us silently get a new one without
            # bothering the user. This is the common "everyday" path
            # after the very first login.
            creds.refresh(Request())
        else:
            # No usable token at all -> do the full interactive login.
            # credentials.json (from Google Cloud Console) tells Google
            # which app is asking. run_local_server() spins up a
            # temporary local webpage, opens your browser, and waits
            # for you to approve access.
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        # Step 3: persist the credentials (access + refresh token) so
        # we don't have to repeat this next time we run the script.
        with open("token.json", "w") as f:
            f.write(creds.to_json())

    # build() constructs the actual API client:
    #   "calendar" = which Google API (Calendar, not Gmail/Drive/etc.)
    #   "v3"       = which version of that API
    #   credentials= how we authenticate each request
    return build("calendar", "v3", credentials=creds)


def list_events(max_results=10):
    """Print the next `max_results` upcoming events on the primary calendar."""
    service = get_service()

    # This builds and sends an HTTP GET request to Google's servers.
    # calendarId="primary" = the user's main calendar (not a shared one).
    # singleEvents=True    = expand recurring events into individual
    #                         instances instead of one repeating block.
    # orderBy="startTime"  = sort chronologically (only valid combined
    #                         with singleEvents=True).
    # .execute() actually fires the request; everything before it just
    # builds up the request object.
    response = service.events().list(
        calendarId="primary",
        maxResults=max_results,
        singleEvents=True,
        orderBy="startTime",
    ).execute()

    # The API returns a dict. The events themselves live under "items".
    events = response.get("items", [])

    for e in events:
        # All-day events have a "date" (e.g. "2026-07-10") instead of
        # a "dateTime" (e.g. "2026-07-10T14:00:00+08:00"), so we check
        # both and use whichever is present.
        start = e["start"].get("dateTime", e["start"].get("date"))
        print(start, "-", e.get("summary", "(no title)"))


def create_event(summary, start, end):
    """Create a new event on the primary calendar."""
    service = get_service()

    # This dict is the event's data, structured the way Google's API
    # expects. "summary" is the event title. start/end need timezone
    # info in the datetime string (e.g. "+08:00" or "Z" for UTC) —
    # otherwise Google will reject or misinterpret the request.
    event = {
        "summary": summary,
        "start": {"dateTime": start},
        "end": {"dateTime": end},
    }

    # .insert() builds an HTTP POST request with `event` as the body;
    # .execute() sends it. The response is the created event, including
    # a generated "id" and a "htmlLink" you can open in a browser.
    result = service.events().insert(calendarId="primary", body=event).execute()
    print("Created:", result.get("htmlLink"))


if __name__ == "__main__":
    # This block only runs when you execute this file directly
    # (not when it's imported elsewhere).
    list_events()

    # Uncomment to try creating an event:
    create_event("Team sync", "2026-07-10T14:00:00+08:00", "2026-07-10T15:00:00+08:00")