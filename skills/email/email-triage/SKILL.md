---
name: email-triage
description: Manage email triage using custom scripts.
---

# email-triage

This skill automates email management using your custom Python scripts.

## Usage
- **Fetch unseen emails:** Run `python3 /root/.hermes/scripts/himalaya/get_unseen_emails.py`
- **Mark all emails as seen:** Run `python3 /root/.hermes/scripts/himalaya/mark_all_emails_seen.py`

## Automation
These scripts are linked to your cron job for automated runs.

## Pitfalls & Notes
- If running manually via terminal, ensure you are in the project root or use the full path to the scripts in `/root/.hermes/scripts/himalaya/`.
- Ensure all email-related script locations are correctly configured in cron to maintain sync.
