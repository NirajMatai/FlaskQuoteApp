# Import the tools we need
from flask import Flask, render_template, request
import requests # This is the library we use to make web requests

# Initialize our Flask app
app = Flask(__name__)

# This is the URL of the free Quote API
QUOTE_API_URL = "https://api.quotable.io/random"

# This is the main route for our webpage
@app.route('/', methods=['GET', 'POST'])
def index():
    # Set default empty values for the quote
    quote_text = ""
    quote_author = ""

    # Check if the user clicked the button on our webpage
    if request.method == 'POST':
        # Make a request to the Quote API
        response = requests.get(QUOTE_API_URL)
        # Parse the JSON response into a Python dictionary
        data = response.json()

        # Get the quote content and author from the dictionary
        quote_text = data['content']
        quote_author = data['author']

    # Render the HTML page, passing the quote data to it
    return render_template('index.html', quote=quote_text, author=quote_author)


if __name__ == '__main__':
    app.run(debug=True)