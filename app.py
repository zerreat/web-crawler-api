import os
import json
from flask import Flask, request, jsonify, send_file
from crawler import crawl

app = Flask(__name__)

# Create a route for the crawl API
@app.route('/crawl', methods=['POST'])
def crawl_endpoint():
    data = request.json
    root_url = data.get('root_url')
    depth = data.get('depth', 2)

    if not root_url:
        return jsonify({"error": "root_url is required"}), 400

    # Call the crawl function
    crawled_links = crawl(root_url, depth)

    # Save the crawled links to a JSON file
    file_path = 'crawled_links.json'
    with open(file_path, 'w') as json_file:
        json.dump({"crawled_links": crawled_links}, json_file)

    # Send the JSON file as a response
    return send_file(file_path, as_attachment=True, download_name='crawled_links.json')

if __name__ == '__main__':
    app.run(debug=True)
