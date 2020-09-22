from flask import Flask, request, render_template, abort # noqa
from dotenv import load_dotenv # noqa
import os
import requests # noqa

load_dotenv()
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


# Home
@app.route('/', methods=["GET"])
def home():
    return render_template("index.html")


# Timeline
@app.route('/timeline', methods=["GET"])
def timeline():
    username = request.args.get('username')
    url = 'https://api.github.com/users/' + username + '/repos'
    repos = []
    data = requests.get(url).json()

    for repo in data:
        created = repo['created_at']

        repos.append({
            'title': repo['name'],
            'desc': repo['description'],
            'created': created[:created.find('T')],
            'url': repo['html_url']
        })

    repos = sorted(repos, key=lambda repo: repo['created'])
    return render_template("timeline.html", repos=repos)


if __name__ == '__main__':
    app.run()
