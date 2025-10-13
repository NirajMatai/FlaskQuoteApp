# Import the tools we need
from flask import Flask, render_template, request
import random # We'll use the random library to pick a quote

# Initialize our Flask app
app = Flask(__name__)

# THIS IS OUR NEW "FAKE" API. IT'S JUST A LIST OF QUOTES.
FAKE_QUOTES = [
    {"author": "Walt Disney", "quote": "The way to get started is to quit talking and begin doing."},
    {"author": "Nelson Mandela", "quote": "The greatest glory in living lies not in never falling, but in rising every time we fall."},
    {"author": "Steve Jobs", "quote": "Your time is limited, so don't waste it living someone else's life."},
    {"author": "Eleanor Roosevelt", "quote": "The future belongs to those who believe in the beauty of their dreams."}
]

# This is the main route for our webpage
@app.route('/', methods=['GET', 'POST'])
def index():
    # Set default empty values for the quote
    quote_text = ""
    quote_author = ""

    # Check if the user clicked the button on our webpage
    if request.method == 'POST':
        # INSTEAD OF CALLING THE INTERNET, WE JUST PICK A RANDOM QUOTE FROM OUR LIST
        random_quote_data = random.choice(FAKE_QUOTES)
        quote_text = random_quote_data['quote']
        quote_author = random_quote_data['author']

    # Render the HTML page, passing the quote data to it
    return render_template('index.html', quote=quote_text, author=quote_author)


if __name__ == '__main__':
    app.run(debug=True)