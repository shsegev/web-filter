from flask import Flask, request, render_template
from requests import get

from plugin_manager import PluginManager, init_plugins
from config import Config
from utils.logger import init_logger, Logger

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    conf = Config()
    if conf.params['enabled'] and conf.params['direction'] != "outbound":
        if not inspect_request():
            return render_template("403.html")
    resp = get(f'{request.base_url}{path}').content
    if conf.params['enabled'] and conf.params['direction'] != "inbound":
        if not inspect_response():
            return render_template("403.html")
    return resp


def inspect_request():
    pl_mgr = PluginManager()
    return pl_mgr.filter(request, True)


def inspect_response():
    pl_mgr = PluginManager()
    return pl_mgr.filter(request, True)


if __name__ == '__main__':
    # TODO set logs relative to current folder
    init_logger("", "/home/shai/repos/web-filter/logs/filter.log")
    logger = Logger("main")
    logger.info("Filter Started")
    init_plugins()
    app.run(host='0.0.0.0', port=8080)
