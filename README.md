
# EventHub — College Event Management System

## Project Overview
EventHub is a web-based college event management system designed to display college events and their details in one place.

## Problem Statement
Students may find it difficult to access event information from different sources. EventHub aims to organize event details such as name, description, date, venue, organizer, and category on a single website.

## Technologies Used
- Python
- Flask
- SQLite
- HTML
- CSS
- Git and GitHub

## Current Features
- Displays college event information on the homepage.
- Fetches event records from an SQLite database.
- Uses Flask to connect the backend with HTML templates.
- Uses CSS to style the website.

## Project Structure
```text
EventHub/
├── app.py
├── database.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── .gitignore
```

## Run Locally
1. Install Python.
2. Install Flask:
   `pip install flask`
3. Initialize the database using the project's database setup code.
4. Start the application:
   `python app.py`
5. Open `http://127.0.0.1:5000` in your browser.

## Team
- Hemang — Team Lead and Frontend Coordinator
- Saransh Sharma — Backend and Database
- Dhruv Singh Solanki — QA and DevOps

## Project Status
The initial application and database integration are under development. Additional features, testing, and deployment will be added as the project progresses.
