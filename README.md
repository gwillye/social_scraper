# Social Follower Scraper

I built this while working in Business Intelligence at a marketing agency, as the social-data collection piece of a larger Python BI/ETL stack (web scraping, Pandas, Google Cloud Storage and Looker Studio). That stack powered 10 market studies and 25 client diagnostics, cut diagnosis time by about 25%, and contributed to more than R$2M in new contracts. This repository is just the part that collects the social data.

The scraper itself is small and focused: it pulls companies' social-media follower counts from search-engine results and computes how those counts change over time. That gives you the raw input for competitive social benchmarking, comparing a brand against its competitors.

## What it does

It resolves a target company's social presence from search results (Google, then LinkedIn) and extracts the follower count using `requests` and `BeautifulSoup`. It then tracks growth and variation between snapshots, so you can see how a brand moves relative to its competitors over time.

## How it works

The collection logic lives in a few collector variants, `coleta.py`, `coleta_seguidores.py` and `coleta_teste.py`. Each one runs a search and then applies a regex to pull out the "followers" figure from the results.

There is also a notebook version, `Coleta_LinkedIn.ipynb`, which can optionally write its output to a Google Sheet.

Finally, `porcentagens.py` handles the percentage-variation calculation between two collections.

## How to run

```bash
pip install requests beautifulsoup4 pandas
# edit the search term to the target company, then:
python coleta_seguidores.py
```

For the Google Sheet output, set your own Sheet ID and Google credentials. These are kept out of version control via `.gitignore`.

## Stack

Python, requests, BeautifulSoup, Pandas, Google Sheets API.
