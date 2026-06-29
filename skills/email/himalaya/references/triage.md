# Email Triage Workflow

For automated triage (cron jobs), do not use raw `himalaya` output directly if you need to filter for unread (unseen) items. Use a shell script wrapper that filters for unflagged items or uses specific backend flags to exclude 'seen' emails.

## Preferred Triage Pattern
When building triage scripts:
1. Ensure the script filters for unread/unseen emails specifically (e.g., `himalaya envelope list not flag seen -o json`).
2. If using Python or shell for the triage, structure the final output as:
   ✉️ [ID]
   Subject: [Subject]
   From: [From]
   
   (Include extra newlines between entries).
3. Always prefer absolute paths for the `himalaya` binary and configuration file in automated jobs to avoid environment/PATH issues.
4. If a script needs to be run by cron, avoid `no_agent: true` if the script relies on environment variables or complex path-dependent binaries — use an agent-managed prompt that sets the environment or use absolute paths for all internal tools.
