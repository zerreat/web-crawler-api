import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl(url, depth):
    crawled_links = set()

    def recursive_crawl(current_url, current_depth):
        if current_depth > depth or current_url in crawled_links:
            return
        
        try:
            response = requests.get(current_url)
            if response.status_code !=200:
                return
            
            crawled_links.add(current_url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract and normalize links

            for link in soup.find_all('a', href=True):
                absolute_link = urljoin(current_url, link['href'])
                if absolute_link not in crawled_links:
                    recursive_crawl(absolute_link, current_depth + 1)

        except requests.RequestException:
            return
    
    recursive_crawl(url, 0)
    return list(crawled_links)
            
