from flask import Flask
from recommendations import Recommendation

app = Flask(__name__)

class Api:
    def __init__(self):
        self.recommendation = Recommendation()
    
    @app.route("/")
    def test():
        return '<p>Working</p>'

    @app.route("/random-recommendations")
    def random_recommendations():
        rp = Recommendation()
        return f'<p>{rp.generate_random_playlist()}</p>'

if __name__ == '__main__':
    app = Api()
    app.run(debug=True)