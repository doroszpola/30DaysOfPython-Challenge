from flask import Flask, render_template, request, redirect, url_for
import os
import re
from collections import Counter

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def home ():
    techs = ['HTML', 'CSS', 'Fask', 'Python']
    name = 'First site'
    return render_template('home.html', techs = techs, name = name, title ='Home')

@app.route('/about')
def about ():
    name = 'First site'
    return render_template('about.html', name = name, title = 'About me')


@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/post', methods = ['GET', 'POST'])
def post ():
    name = 'Text Analyzer'
    if request.method == 'GET':
        return render_template('post.html', name = name, title = name)
    if request.method == 'POST':
        content = request.form['content']

        text_len = len(content)
        words = re.findall(r'\b[A-Za-z]+\b',content)  #start at word boundary collect all A-Z, a-z, 0-9, _ characters and end on another boundary
        counts = Counter(words).most_common(10)

        
        return render_template('result.html', text_len = text_len, counts = counts)



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
