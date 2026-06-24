# 🕸️ Automated Web Scraper with CLI

## 📝 Introduction
This project is an automated **Web Scraper** built in Python using **Requests** and **BeautifulSoup4**. It is designed to navigate a bookstore sandbox website, handle multi-page pagination seamlessly, manage missing data gracefully, and export structured product information directly into clean CSV or JSON formats.

---

## 🚀 Key Features
* **Dynamic Pagination:** Automatically detects, calculates, and traverses through "Next" page links.
* **Error Resilience:** Gracefully catches network timeouts (`HTTPError`) and handles missing HTML tags without crashing the script.
* **Polite Scraping:** Implements artificial throttling (`time.sleep`) to respect host servers and avoid IP blocking.
* **Full CLI Support:** Completely customizable through command-line arguments (file names, formats, and page limits).

---

## 🛠️ Step-by-Step Installation

Follow these steps to set up the project on your local machine:

### Step 1: Prerequisites
Make sure you have **Python 3.x** installed on your system. You can check this by running `python --version` in your terminal.

### Step 2: Install Dependencies
Clone or download this repository, open your terminal/command prompt inside the project folder, and run:
```bash
pip install -r requirements.txt
💻 How to Run the ProjectMethod 1: Automated Execution (One-Click Setup)If you want the script to automatically handle everything:Windows Users: Simply double-click run.bat or execute it via Command Prompt.Mac/Linux Users: Open your terminal, give execution permission, and run the shell script:Bashchmod +x run.sh
./run.sh
Method 2: Manual CLI Customization (Step-by-Step)You can control the scraper directly from your terminal using custom parameters:To run with default settings (Scrapes 3 pages and outputs a CSV):Bashpython scraper.py
To scrape 5 pages and save explicitly as JSON:Bashpython scraper.py --output dataset.json --format json --max-pages 5
To view the Help Menu (Displays all available arguments and flags):Bashpython scraper.py --help
📊 Output Format PreviewThe extracted data will be formatted cleanly into columns (CSV) or key-value pairs (JSON) like this:TitlePriceAvailabilityA Light in the Attic£51.77In stockTipping the Velvet£53.74In stockSoumission£50.10In stock📁 Project StructurePlaintext├── scraper.py          # Main application logic & parsing functions
├── requirements.txt    # List of external Python packages needed
├── run.bat            # Windows automation batch file
├── run.sh             # Linux/macOS automation shell script
└── README.md          # Project documentation (this file)
🎯 ConclusionThis web scraper serves as an efficient, automated data collection tool. By combining programmatic web requests with robust parsing and error-handling mechanisms, it eliminates the need for tedious manual data entry. Whether used for simple data logging, price comparison engines, or scaling up into data analysis workflows, it provides a stable and modular foundation for any web scraping requirements.




