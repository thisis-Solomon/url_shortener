import random
import string
from flask import Flask, redirect, request, render_template
from model import (
    init_db,
    get_url,
    get_all_urls,
    insert_url,
    delete_url,
    increment_visit_count
    )

app = Flask(__name__)

init_db()

def generate_short_code(length = 6):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        original_url = request.form['url']
        short_code = generate_short_code()
        insert_url(original_url, short_code)
        return redirect('/')
    all_url = get_all_urls()

    return render_template('index.html', all_urls = all_url)

@app.route("/<short_code>")
def redirect_url(short_code):
    url_data = get_url(short_code)
    if url_data:
        increment_visit_count(short_code)
        return redirect(url_data[1])

    return render_template('404.html'), 404


@app.route('/delete/<short_code>', methods=["POST", "GET"])
def delete(short_code):
    delete_url(short_code)
    return redirect('/')


if __name__ == "__main__":
    app.run(
        debug=True,
        host='0.0.0.0',
        port=8080
        )