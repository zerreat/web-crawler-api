import os
import json
from flask import Flask, request, jsonify, send_file, render_template
from crawler import crawl

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', error=None, success=None, download_link=None)

@app.route('/crawl', methods=['POST'])
def crawl_endpoint():
    root_url = request.form.get('root_url')
    depth = request.form.get('depth', 2)

    if not root_url:
        return render_template('index.html', error="Root URL is required.", success=None, download_link=None)

    try:
        depth = int(depth)
    except ValueError:
        return render_template('index.html', error="Depth must be a number.", success=None, download_link=None)

    try:
        crawled_links = crawl(root_url, depth)
    except Exception as e:
        return render_template('index.html', error="An error occurred during crawling. Please try again.", success=None, download_link=None)

    if not crawled_links:
        return render_template('index.html', error="No links found or invalid URL. Please check and enter the full url including https://www.example.com then try again.", success=None, download_link=None)

    file_path = 'crawled_links.json'
    with open(file_path, 'w') as json_file:
        json.dump({"crawled_links": crawled_links}, json_file)

    return render_template('index.html', error=None, success="File is ready to download.", download_link="/download")

@app.route('/download')
def download_file():
    return send_file('crawled_links.json', as_attachment=True, download_name='crawled_links.json')

if __name__ == '__main__':
    app.run(debug=True)
