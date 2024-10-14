import os
import json
from flask import Flask, request, jsonify, send_file, render_template
from crawler import crawl

app = Flask(__name__)

# Route for displaying the HTML form
@app.route('/')
def index():
    return render_template('index.html')

# Create a route for the crawl API
@app.route('/crawl', methods=['POST'])
def crawl_endpoint():
    # Check if form data was submitted
    root_url = request.form.get('root_url')
    depth = request.form.get('depth', 2)

    if not root_url:
        return jsonify({"error": "root_url is required"}), 400

    # Ensure depth is an integer
    try:
        depth = int(depth)
    except ValueError:
        return jsonify({"error": "Depth must be a number"}), 400

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
