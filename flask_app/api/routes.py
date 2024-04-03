import os
import json
from flask import render_template, request,make_response, Blueprint, url_for

api = Blueprint("api", __name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
with open(f"{APP_ROOT}/resources/sample.json") as f:
    tickers = json.load(f)

@api.route("/api/v1/search", methods=["POST"])
def search():
    search_term = request.form.get("search")

    if not len(search_term):
        return render_template("test_table.html", tickers=[])

    res_tickers = []
    for ticker in tickers["data"]:
        if search_term.lower() in ticker["name"].lower():
            res_tickers.append(ticker)

    return render_template("test_table.html", tickers=res_tickers)