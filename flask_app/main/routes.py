import json
import os
from flask import render_template, request,make_response, Blueprint

main = Blueprint("main", __name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
with open(f"{APP_ROOT}/resources/sample.json") as f:
    tickers = json.load(f)

@main.route("/", methods=["GET", "POST"])
@main.route("/index", methods=["GET", "POST"])
def index():

    return render_template("index.html", title="welcome")


@main.route("/search", methods=["POST"])
def search_tickers():
    search_term = request.form.get("search")

    if not len(search_term):
        return render_template("test_table.html", tickers=[])

    res_tickers = []
    for ticker in tickers["data"]:
        if search_term.lower() in ticker["name"].lower():
            res_tickers.append(ticker)

    return render_template("test_table.html", tickers=res_tickers)


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