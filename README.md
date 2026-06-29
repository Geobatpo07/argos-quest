# Argos Quest

Argos Quest is a Streamlit dashboard for aggregating and tracking thesis opportunities from configured sources, starting with INRIA. It synchronizes scraped offers into a DuckDB database and displays basic collection statistics in a small operations-focused interface.

## Overview

- Scrapes thesis offers from the configured sources.
- Stores normalized data in DuckDB.
- Displays a dashboard with synchronization controls and thesis counts.
- Uses a modular layout with application services, infrastructure adapters, and UI pages.

## Tech Stack

- Python 3.13+
- Streamlit
- DuckDB
- Requests
- BeautifulSoup / lxml / selectolax
- Polars
- Pydantic

## Project Structure

- `app.py` - Streamlit entry point.
- `ui/` - Dashboard pages and reusable UI components.
- `application/` - Use cases and services.
- `infrastructure/` - Database, HTTP, and scraper implementations.
- `domain/` - Core entities, enums, and repository interfaces.
- `data/` - Local DuckDB database files.
- `tests/` - Automated tests.

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -e .
```

3. Copy `.env.example` to `.env` and adjust the values if needed.

## Run

Start the Streamlit app:

```bash
streamlit run app.py
```

## Testing

Run the test suite with:

```bash
pytest
```

## GitHub Description

Suggested repository description:

> Streamlit dashboard for scraping, synchronizing, and tracking thesis opportunities in DuckDB.
