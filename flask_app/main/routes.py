import json
import os
from flask import render_template, request,make_response, Blueprint, url_for

main = Blueprint("main", __name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
with open(f"{APP_ROOT}/resources/sample.json") as f:
    tickers = json.load(f)

@main.route("/", methods=["GET", "POST"])
@main.route("/index", methods=["GET", "POST"])
def index():

    meta = {
        "title": "Home - Flask App",
        "description": "My Flask App",
        "og_url": url_for('main.index', _external=True)
    }

    return render_template("index.html", meta=meta)


@main.route("/search", methods=["POST"])
def search():
    search_term = request.form.get("search")

    if not len(search_term):
        return render_template("test_table.html", tickers=[])

    res_tickers = []
    for ticker in tickers["data"]:
        if search_term.lower() in ticker["name"].lower():
            res_tickers.append(ticker)

    meta = {
        "title": "Home - Flask App",
        "description": "HTMX Dynamic Search",
        "og_url": url_for('main.search', _external=True)
    }

    return render_template("test_table.html", tickers=res_tickers, meta=meta)


@main.route("/sitemap.xml")
def sitemap():
    pages = [
      {"loc": "http://localhost:5000/"},
      {"loc": "http://localhost:5000/search"},
    ]
  
    sitemap_xml = render_template("sitemap_template.xml", pages=pages)
    response = make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"
  
    return response