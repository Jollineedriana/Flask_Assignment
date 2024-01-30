from flask import Flask, render_template, redirect, url_for, request
import time
# creating an instance
app = Flask(__name__)

@app.route('/')
# creating a root page for app
def welcome_message():
    return render_template('index.html')


# ROUTING
# creating additional routes ("\about") and ("\contact")
@app.route('/about')
def about():
    return render_template('about.html')
 
@app.route('/contact')
def contact():
    return render_template('contact.html')

# creating a route ("\user\<username>") with parameter username and displays a personalised message


@app.route('/user/<username>')
def user_identity(username):
    return render_template('user.html')

# Creating a route ("/submit") with a form that takes a user's name and email and On form submission, display a 
# thank you message with the submitted information.

# FORM HANDLING

@app.route('/submit', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        return render_template('thank.html', username=username, email=email)

    return render_template('submit.html')
# activating the debug mode
if __name__ == '__main__':
    app.run(debug=True)
     # python app.py to activate the debug