from flask import Flask
from requests import get

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    return get(f'{""}{path}').content


if __name__ == '__main__':
    # read configuration
    app.run(host='0.0.0.0', port=8080)
