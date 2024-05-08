from flask import Flask
import randomplaylist
app = Flask(__name__)


@app.route("/random-recommendations")
def random_recommendations():
    return f'<p>{randomplaylist.generateRandomPlaylist()}</p>'