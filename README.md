# Web Crawler API

This project is a web crawler API built using Python and Flask. The API allows you to provide a root URL and a depth value, and it returns a JSON file containing all the crawled links up to the specified depth.

## Features
- Recursively crawls websites up to a given depth
- Extracts and returns unique links from the crawled pages
- Returns results as a downloadable JSON file

## Tech Stack
- **Backend**: Flask, Python
- **Web Scraping**: requests, BeautifulSoup

## Installation

To get started with this project, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/your-username/web-crawler-api.git
```
2. Navigate to the project directory:
```bash
cd web-crawler-api
```
3. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
4. Install the required dependencies:
```bash
pip install -r requirements.txt
```
## Usage

1. Start the Flask server:
```bash
python app.py
```
2. Use `curl` or Postman to make a `POST` request to the `/crawl` endpoint with a JSON payload:
```bash
curl -X POST http://127.0.0.1:5000/crawl -H "Content-Type: application/json" -d "{\"root_url\": \"https://example.com\", \"depth\": 2}" --output crawled_links.json
```
3. The API will return a `crawled_links.json` file containing the crawled URLs

## Example Request and Response

### Request:
```bash
{
  "root_url": "https://example.com",
  "depth": 2
}
```

### Response (crawled_links.json):
```bash
{
  "crawled_links": [
    "https://example.com",
    "https://example.com/about",
    "https://example.com/contact"
  ]
}
```


