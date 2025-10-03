# Mystery Books Scraper

This Python script scrapes the mystery books category from [Books to Scrape](https://books.toscrape.com) and extracts the following information for each book:

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

Output example:

```
📚 In the Woods ||| 💰 £19.84 ||| 📦 In stock
==========================================================================================
📚 The Silkworm ||| 💰 £23.88 ||| 📦 In stock
==========================================================================================
...
```

## Notes

* The script scrapes only the first page of the Mystery category. You can modify it to loop through all pages if desired.
* The `strip()` method is used to clean up the availability text.
* Each book is contained in a `<li>` element with class `col-xs-6 col-sm-4 col-md-3 col-lg-3`.

## License

This project is open-source and free to use.

