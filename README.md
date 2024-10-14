# Web Crawler API

This project is a web crawler API built using Python and Flask. The API takes a root URL and a depth value as inputs and returns a JSON file containing all the crawled links up to the specified depth. Additionally, the project provides a simple web interface for users to interact with the API and download the crawled links easily.

## Features
- Recursively crawls websites up to a user-defined depth.
- Extracts and returns unique links from the crawled pages.
- Outputs results as a downloadable JSON file.
- Handles invalid URLs and unreachable pages gracefully.
- Provides an easy-to-use web interface for users to input the URL and depth, and download the result.

## Tech Stack
- **Backend**: Flask (Python)
- **Web Scraping**: requests, BeautifulSoup
- **Frontend**: HTML, CSS, JavaScript

## Installation

To get started with this project, follow these steps:

1. **Clone the repository**:
```bash
git clone https://github.com/zerreat/web-crawler-api.git
```
2. **Navigate to the project directory**:
```bash
cd web-crawler-api
```
3. **Create a virtual environment and activate it**:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
4. **Install the required dependencies**:
```bash
pip install -r requirements.txt
```
## Usage


### Option 2: Using cURL or Postman
1. **Start the Flask server**:
```bashc
python app.py
```
2. **Make a `POST` request to the `/crawl` endpoint**:
* You can use `curl` or Postman to send the request. Here’s an example using `curl`:
```bash
curl -X POST http://127.0.0.1:5000/crawl -H "Content-Type: application/json" -d "{\"root_url\": \"https://example.com\", \"depth\": 2}" --output crawled_links.json
```

* Alternatively, use Postman:
  * Set method to `POST`.
  * Set the URL to `http://127.0.0.1:5000/crawl`.
  * In the Body tab, choose `raw` and set it to JSON format. Then, add the JSON payload:
```bash
{
  "root_url": "https://example.com",
  "depth": 2
}

```

3. **The API will return a `crawled_links.json` file containing the URLs it found.**

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

## Error Handling

* If an invalid URL is provided, the API will return an error response.

* Depth values that are too large will result in limited crawling, depending on the website's structure and accessibility.

## Frontend (User Interface)
The application also includes a simple frontend interface built with HTML, CSS, and JavaScript, allowing users to easily interact with the API.
* Submit Form: Users can submit the URL and depth using the web form, and see a loading indicator while the crawl is in progress.
* Download Links: Once the crawling process is completed, a download link is provided to retrieve the crawled_links.json file.

## Frontend File Structure:

* HTML: Provides the structure and layout of the web interface.
* CSS: Defines the styling, including responsive design for mobile devices.
* JavaScript: Implements AJAX functionality to submit the form without reloading the page, displays a loading spinner, and handles the abort button.

## License

**This project is licensed under the MIT License - see the `LICENSE` file for details.**


## Key Enhancements:
- **Introduction**: Added a bit more context about why the tool is useful.
- **Installation**: Slightly clarified steps.
- **Error Handling**: Mentioned how the API handles errors, which shows that the project has some robustness.
- **License**: Added a license section (optional, depending on whether you want to include a license).
