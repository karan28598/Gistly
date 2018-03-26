from flask import Flask
import minify as minify
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
 
app = Flask(__name__)
 
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/parameterExtraction')
def parameterExtraction():
    if request.method == 'GET':
        parsed_url = request.args['link']
        result = minify.final(parsed_url)
        return render_template("result.html")


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='127.0.0.1', port=4000)
