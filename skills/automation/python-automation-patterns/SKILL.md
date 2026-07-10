---
name: python-automation-patterns
description: Guidelines for writing portable Python automation scripts for Hermes Agent, handling `hermes_tools` vs standalone CLI calls.
---

# Python Automation in Hermes Agent

Strategies for writing and running Python scripts within the Hermes Agent environment, focusing on portable code and proper integration.

## Key Concepts
- **`hermes_tools` vs. Standard Python:**
  - `hermes_tools` is available ONLY when running scripts via the agent's `execute_code` tool. 
  - For standalone scripts intended to run directly in the terminal (e.g., via `cron`), use external CLI tools (like `himalaya` or `curl`) via Python's `subprocess` module.
- **Portability:**
  - Never hardcode unique identifiers (e.g., Telegram Chat IDs). 
  - Load sensitive configuration from environment variables (e.g., `.env` files).
- **Automation Pattern:**
  - Prefer "no-agent" cron jobs for routine, low-reasoning tasks to conserve API quota.
  - Use `subprocess.run(..., shell=True)` for calling existing CLI tools from Python scripts.

## Verification
- Test scripts using `execute_code` first to leverage `hermes_tools`.
- For standalone CLI scripts, run them manually in the terminal to ensure they handle standard environment dependencies correctly.
