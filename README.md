Web Scraper Project
A robust, automated web scraper built in Python using BeautifulSoup and Requests. It is designed to extract book details (titles, prices, and availability) from a sandbox bookstore website, handle pagination across multiple pages, and save the structured data into a CSV or JSON file.

Features
Automated Pagination: Automatically detects and navigates to the "Next" page.

Error Handling: Gracefully handles missing data tags and network request timeouts without crashing.

Flexible Exports: Supports saving data in both CSV and JSON formats.

CLI Interface: Allows customization of output filenames, formats, and maximum page limits directly from the terminal.

Installation
Make sure you have Python installed, then install the required dependencies:

Bash


pip install requests beautifulsoup4
How to Run
1. One-Click Automated Run
Windows: Double-click run.bat (or run run.bat inside Command Prompt).



2. Custom CLI Run
You can also run the script manually with custom arguments:

Default settings (Scrapes 3 pages to books_scraped.csv):

Bash


python scraper.py
Scrape 5 pages and save as JSON:

Bash


python scraper.py --output results.json --format json --max-pages 5
View help options:

Bash


python scraper.py --help
