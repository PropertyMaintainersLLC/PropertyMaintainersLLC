from pm import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact_us():
    return render_template('contactus.html')

@app.route('/testimonials')
def testimonial():
    return render_template('testimonials.html')