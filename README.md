# Mystery Books Scraper

This Python script scrapes the mystery books category from [Books to Scrape](https://books.toscrape.com) and extracts the following information for each book across **all pages**:

* Title
* Price
* Availability

It prints the information in a clean and readable format.

## Technologies Used

* Python 3
* `requests` library for HTTP requests
* `BeautifulSoup` from `bs4` for HTML parsing
* `lxml` parser for BeautifulSoup

## Installation

1. Clone the repository or download the script.
2. Install the required libraries if you haven't already:

```bash
pip install requests beautifulsoup4 lxml
```

## Usage

Run the script using Python:

```bash
python scrape_mystery_books.py
```

The script will automatically loop through all paginated pages in the Mystery category and scrape every book.

Output example:

```
📚 In the Woods ||| 💰 £19.84 ||| 📦 In stock
==========================================================================================
📚 The Silkworm ||| 💰 £23.88 ||| 📦 In stock
==========================================================================================
...
```

## How It Works

* The script starts from page 1 and dynamically builds the URL for subsequent pages.
* It stops scraping when there are no more pages (HTTP 404).
* Each book is contained in a `<li>` element with class `col-xs-6 col-sm-4 col-md-3 col-lg-3`.
* The `strip()` method is used to clean up the availability text.

## Notes

* This approach ensures all books in the Mystery category are scraped, regardless of the number of pages.
* You can further modify the script to save the scraped data to CSV, JSON, or a database.

## License

This project is open-source and free to use.
