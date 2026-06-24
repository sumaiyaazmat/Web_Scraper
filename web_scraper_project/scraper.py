import argparse
import csv
import json
import sys
import time
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/catalogue/page-1.html"

def fetch_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"[Error] Failed to fetch {url}: {e}", file=sys.stderr)
        return None

def parse_page(html, current_url):
    soup = BeautifulSoup(html, "html.parser")
    books = []
    book_elements = soup.find_all("article", class_="product_pod")

    for element in book_elements:
        try:
            title_el = element.h3.a if element.h3 else None
            title = title_el["title"] if title_el and title_el.has_attr("title") else "Unknown Title"

            price_el = element.find("p", class_="price_color")
            price = price_el.text.strip() if price_el else "N/A"

            avail_el = element.find("p", class_="instock availability")
            availability = avail_el.text.strip() if avail_el else "Unknown"

            books.append({
                "title": title,
                "price": price,
                "availability": availability
            })
        except Exception as e:
            print(f"[Warning] Skipped a book due to parsing error: {e}")

    next_button = soup.find("li", class_="next")
    next_url = None
    if next_button and next_button.a:
        next_page_rel = next_button.a["href"]
        next_url = urljoin(current_url, next_page_rel)

    return books, next_url

def save_data(data, filename, file_format):
    if not data:
        print("[Info] No data to save.")
        return

    if file_format == "csv":
        keys = data[0].keys()
        with open(filename, "w", newline="", encoding="utf-8") as f:
            dict_writer = csv.DictWriter(f, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)
    elif file_format == "json":
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"[Success] Saved {len(data)} items to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Scrape book data from books.toscrape.com")
    parser.add_argument("-o", "--output", default="books_scraped.csv", help="Output filename")
    parser.add_argument("-f", "--format", choices=["csv", "json"], default="csv", help="Output file format")
    parser.add_argument("-m", "--max-pages", type=int, default=3, help="Maximum number of pages to scrape")

    args = parser.parse_args()

    all_books = []
    current_url = BASE_URL
    page_count = 0

    print(f"Starting scraper. Target max pages: {args.max_pages}")

    while current_url and page_count < args.max_pages:
        page_count += 1
        print(f"Scraping Page {page_count}: {current_url}...")

        html = fetch_page(current_url)
        if not html:
            break

        books, next_url = parse_page(html, current_url)
        all_books.extend(books)
        current_url = next_url

        if current_url:
            time.sleep(1)

    save_data(all_books, args.output, args.format)

if __name__ == "__main__":
    main()
