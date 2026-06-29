# Research Paper Parsing and Fetching

This reference captures the current workflow for managing ArXiv research papers.

## fetch_papers.py
- **Role:** Main entry point for fetching papers. Handles API calls, parses XML response on-the-fly, and outputs JSON.
- **Location:** `/root/.hermes/scripts/papers/fetch_papers.py`

## parse_papers.py
- **Role:** Legacy/Manual script. Requires a local `papers.xml` file.
- **Status:** Redundant in the automated `fetch_papers.py` workflow. Retained only for potential manual debug use.

## Formatting Standard
- All summaries must be formatted using the `science-briefing-formatter` skill to ensure consistency in research updates.
