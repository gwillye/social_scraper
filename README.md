# Social Follower Scraper

> **Real-world context.** Built while working in **Business Intelligence at Macfor**, where I developed a Python BI/ETL stack (web scraping + Pandas + Google Cloud Storage + **Looker Studio**) that powered 10 market studies and 25 client diagnostics — cutting diagnosis time by **~25%** and contributing to **+R$2M in new contracts**, with coverage in major outlets (O Globo / UOL). This repository is the **social-data collection** component of that work.

A small, focused scraper that pulls companies' **social-media follower counts** from search-engine results and computes their variation over time — the raw input for competitive social benchmarking.

## What it does
- Resolves a target company's social presence from **search results** (Google → LinkedIn) and extracts the **follower count** with `requests` + `BeautifulSoup`.
- Tracks **growth/variation** between snapshots to benchmark a brand against competitors.

## How it works
- `coleta.py` / `coleta_seguidores.py` / `coleta_teste.py` — collector variants (search → regex for the "followers" figure).
- `Coleta_LinkedIn.ipynb` — notebook version, with optional write-out to a Google Sheet.
- `porcentagens.py` — percentage-variation calculation between collections.

## How to run
```bash
pip install requests beautifulsoup4 pandas
# edit the search term to the target company, then:
python coleta_seguidores.py
```
For the Google Sheet output, set your own Sheet ID and Google credentials — these are kept out of version control via `.gitignore`.

## Stack
Python · requests · BeautifulSoup · Pandas · Google Sheets API
