---
name: science-briefing-formatter
description: Formatter for arXiv research briefings.
---

# science-briefing-formatter

A standard formatter for scientific research briefings, typically used in cron jobs or research workflows.

## Usage
When summarizing papers (e.g., from arXiv), output them in this format:

### Latest AI/CS arXiv Papers (YYYY-MM-DD)

1. **Title** (ID)
   - *Abstract*: [Brief summary]
   - [PDF Link]

## Pipeline Integration
This formatter expects structured input (Title, ID, Abstract) and produces a clean, readable briefing.
