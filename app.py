from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to URL Shortener"

@app.route('/about')
def about():
    return "This is the about page for the url shortener"

if __name__ == "__main__":
    app.run(debug=True)