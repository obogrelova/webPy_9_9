from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def fetch_quote():
    response = requests.get('http://api.quotable.io/random')
    if response.status_code == 200:
        return response.json()
    else:
        return {"content": "Не удалось получить цитату.", "author": ""}

@app.route('/')
def index():
    quote = fetch_quote()
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True)