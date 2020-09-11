from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os.path

app = Flask(__name__)
app.secret_key = '4872348234btgfdhgfdg' #this is random secret key for just public repository and development purposes

@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/your-url', methods=['GET', 'POST'])
def your_url():
    if request.method == 'POST':
        urls = {}
        if os.path.exists('urls.json'):
            with open('urls.json') as urls_file:
                urls = json.load(urls_file)
        urls[request.form['code']] = {'url': request.form['url']}

        if request.form['code'] in urls.keys():
            flash('That shortcut already exists')
            return redirect(url_for('hello_world'))

        with open('urls.json', 'w') as url_file:
            json.dump(urls, url_file)
        return render_template('your_url.html', code=request.form['code'])
    return redirect(url_for('hello_world'))


if __name__ == '__main__':
    app.run(debug=True)
