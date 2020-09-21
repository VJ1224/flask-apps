from flask import Flask, request, render_template, abort # noqa
from dotenv import load_dotenv # noqa
import os
import requests # noqa


load_dotenv()
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


# Home
@app.route('/')
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
