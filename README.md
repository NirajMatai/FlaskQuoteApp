# Random Quote Generator 

A simple Flask-based web application that generates random motivational quotes with the click of a button.

Built as a beginner-friendly project to explore:
- Flask fundamentals
- Backend ↔ frontend interaction
- HTML templating
- Form handling
- Dynamic content rendering in Python web apps

## Features 

- Generates a random quote on button click
- Simple and clean Flask backend
- Uses local quote storage (no external API required)
- Beginner-friendly project structure
- Fast and lightweight



## Tech Stack 

- Python
- Flask
- HTML (Jinja templating)



## Project Structure 

```plaintext
project-folder/
│
├── app.py
├── templates/
│   └── index.html
└── README.md
```



## How It Works 

1. User opens the webpage
2. Flask serves the HTML page
3. User clicks the “Generate Quote” button
4. A random quote is selected from a predefined list
5. The quote and author are displayed dynamically



## Sample Quote Data 

```python
FAKE_QUOTES = [
    {
        "author": "Steve Jobs",
        "quote": "Your time is limited, so don't waste it living someone else's life."
    }
]
```



## Installation & Setup 

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd <repo-name>
```

### 2. Install Flask

```bash
pip install flask
```

### 3. Run the application

```bash
python app.py
```

### 4. Open in browser

```plaintext
http://127.0.0.1:5000
```



## Concepts Learned 

This project helped in understanding:

- Flask routing
- GET and POST requests
- Request handling
- Jinja templates
- Python lists & dictionaries
- Random data generation
- Basic backend development
