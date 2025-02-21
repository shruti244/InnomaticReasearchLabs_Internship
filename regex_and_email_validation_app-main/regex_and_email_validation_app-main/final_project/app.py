from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    # Home page with links to the email validator and regex matcher
    return render_template('home_page.html')

@app.route('/regex_page', methods=['GET', 'POST'])
def regex_page():
    results = None
    messages = None
    if request.method == 'POST':
        pattern = request.form.get('pattern')
        text = request.form.get('text')
        if pattern and text:
            results = re.findall(pattern, text)
            if not results:
                messages = 'No matches found.'
    return render_template('regex_page.html', results=results, messages=messages)

@app.route('/email', methods=['GET', 'POST'])
def email():
    message = ''
    if request.method == 'POST':
        email = request.form.get('email')
        if email:
            if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
                message = 'Valid email address!'
            else:
                message = 'Invalid email address!'
        else:
            message = 'Email address not provided!'
    return render_template('email.html', message=message)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")




