from datetime import datetime
import multiprocessing
import os

import flask
import requests

webapp = flask.Flask(__name__)


lock = multiprocessing.RLock()
MAX_AGE_SECONDS = 5


@webapp.route("/")
def home():
    with lock:
        filename = "img.jpg"
        t_modified = datetime.fromtimestamp(os.path.getmtime(filename))
        dt = datetime.now() - t_modified
        if dt.total_seconds() > MAX_AGE_SECONDS:
            ip_address = "192.168.87.206"
            numbers_and_letters = "wuuPhkmUCeI9WG7C"
            username = "viewer"
            password = "Viewer00"

            url = f"http://{ip_address}/cgi-bin/api.cgi?cmd=Snap&channel=0&rs={numbers_and_letters}&user={username}&password={password}"
            resp = requests.get(url)
            if resp.status_code == 200:
                with open(filename, "wb") as f:
                    f.write(resp.content)

        if os.path.exists(filename):
            return flask.send_file(filename, mimetype="image/jpeg")
        else:
            return "Webcam image could not be retrieved", 404


@webapp.route("/status")
def status():
    return "Ok"
