@echo off
echo Setting up Python Environment...
python -m venv venv
call venv\Scripts\activate
echo Installing required dependencies...
pip install -r requirements.txt
echo Running the Web Scraper...
python scraper.py --max-pages 2 --output scraped_books.csv --format csv
echo Done! Data saved to scraped_books.csv
pause




