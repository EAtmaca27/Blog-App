### Masterblog

A simple Flask blog app where you can view, add, update, and delete blog posts.
Posts are stored in a local JSON file (no database needed).

### Features

- View all blog posts on the home page
- Add a new post via /add
- Edit an existing post via /update/<id>
- Delete a post via /delete/<id>

### Setup

1. Install Flask:
   pip install flask

2. Run the app from the Blog-App directory:
   python app.py

3. Open your browser and go to:
   http://localhost:5000

### Project Structure

Blog-App/
├── app.py               # Flask routes and logic
├── data/
│   └── posts.json       # Blog post storage
├── templates/
│   ├── index.html       # Home page
│   ├── add.html         # Add post form
│   └── update_form.html # Update post form
└── static/
    └── style.css        # Styling