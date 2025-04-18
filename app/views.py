from app import app
from flask import render_template, request, redirect, url_for, flash
import datetime

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/profile/')
def profile():
    """Render the user's profile page."""
    date_joined = datetime.date(2019, 2, 7)  # Example date
    formatted_date = format_date_joined(date_joined)
    return render_template('profile.html', date_joined=formatted_date)

def format_date_joined(date):
    """Format the date as Month, Year."""
    return date.strftime("%B, %Y")

@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
