from flask import Flask, request, render_template, flash, jsonify
from jinja2 import StrictUndefined
import os
from functions.source import count_tags, source_text

app = Flask(__name__)

app.secret_key = os.environ.get("FLASK_SECRET_KEY", "ABCDEF")
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def home():
    """Home page"""

    return render_template("index.html")


@app.route("/count-tags.json")
def count_tags_JSON():
    """ Prepares JSON with tag counts of URL in search bar """

    url = request.args.get("source")

    return jsonify(count_tags(url))


@app.route("/source-text.json")
def source_text_JSON():
    """ Prepares JSON with source text of URL in search bar """

    url = request.args.get("source")

    return source_text(url)


if __name__ == "__main__":
    
    PORT = int(os.environ.get("PORT", 5000))
    DEBUG = "NO_DEBUG" not in os.environ

    app.run(debug=DEBUG, host="0.0.0.0", port=PORT)