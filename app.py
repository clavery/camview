import os
from datetime import datetime

from flask import Flask, render_template


app = Flask(__name__)


def file_view(path):
    pass


def dates_for_files(path):
    active_days = {}
    files = os.listdir(path)

    for f in files:
        mtime = datetime.fromtimestamp(os.path.getmtime(os.path.join(path, f)))
        active_days[mtime.date()] = True

    return list(sorted(active_days.keys(), cmp=lambda x: str(x)))


def files_for_date(date, path):
    mtime = lambda f: os.stat(os.path.join(path, f)).st_mtime
    sorted_files = [(f, datetime.fromtimestamp(os.path.getmtime(os.path.join(path, f))))
                    for f in list(sorted(os.listdir(path), key=mtime))]
    return [(f, d) for (f, d) in sorted_files
            if str(d.date()) == date]


@app.route("/")
def main():
    return render_template("index.html", days=dates_for_files('data'))


@app.route("/<day>")
def day(day):
    print day
    return render_template("files.html", files=files_for_date(day, 'data'))


if __name__ == "__main__":
    app.run(debug=True)
