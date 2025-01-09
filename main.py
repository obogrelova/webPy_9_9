from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

const_url = 'https://api.quotable.io/random'

def get_random_quote():
    params = {
        'method': 'getQuote',
        'format': 'json',
        'lang': 'ru'
    }
    response = requests.get(const_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get('quoteText', 'Цитата не найдена')
    return 'Ошибка при получении цитаты.'

@app.rout('/')
def index():
    quote = get_random_quote()
    return render_template('index.html', quote=quote)

@app.rout('/api/quote')
def quote_api():
    quote = get_random_quote()
    return jsonify({ 'quote': quote })

if __name__ == '__main__':
    app.run(debug=True)