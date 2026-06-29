---
name: science-briefing-formatter
description: Formatter for arXiv research briefings.
---

# science-briefing-formatter

A standard formatter for scientific research briefings, typically used in cron jobs or research workflows. Where there are 4 papers in total. The first 3 are AI/CS papers, and the last 4th paper is the "Wildcard" random category paper.

## Usage
When summarizing papers (e.g., from arXiv), output them in this format:

### Latest AI/CS arXiv Papers (YYYY-MM-DD)

1. **Title** (ID) (Primary Category)
   - *Abstract*: [Brief summary]
   - [PDF Link]


### Wildcard Paper

4. **Title** (ID) (Primary Category)
   - *Abstract*: [Brief summary]
   - [PDF Link]
 

## Pipeline Integration
This formatter expects structured input (Title, ID, primary_category, Abstract) and produces a clean, readable briefing.
