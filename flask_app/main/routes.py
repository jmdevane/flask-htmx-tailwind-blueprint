import os
from flask import render_template, request,make_response, Blueprint, url_for, send_from_directory

main = Blueprint("main", __name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@main.route("/", methods=["GET", "POST"])
@main.route("/index", methods=["GET", "POST"])
def index():

    meta = {
        "title": "Home - Flask App",
        "description": "My Flask App",
        "og_url": url_for('main.index', _external=True)
    }

    return render_template("index.html", meta=meta)


@main.route("/sitemap.xml")
def sitemap():
    pages = [
      {"loc": url_for("main.index", _external=True)},
      {"loc": url_for("main.search", _external=True)},
    ]
  
    sitemap_xml = render_template("sitemap_template.xml", pages=pages)
    response = make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"
  
    return response


@main.route("/robots.txt")
def static_from_root():
    return send_from_directory(current_app.static_folder, request.path[1:])