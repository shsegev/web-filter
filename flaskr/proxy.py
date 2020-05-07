from flask import Flask, request, render_template
from requests import get

from plugin_manager import PluginManager

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    if inspect_request():
        return render_template("403.html")
    resp = get(f'{request.base_url}{path}').content


def inspect_request():
    pl_mgr = PluginManager()
    return pl_mgr.filter(request, True)


def inspect_response():
    pl_mgr = PluginManager()
    return pl_mgr.filter(request, True)


if __name__ == '__main__':
    # read configuration

    app.run(host='0.0.0.0', port=8080)
