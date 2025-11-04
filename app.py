import os
from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv() 
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'fallback-local-key')

@app.route('/')

def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
