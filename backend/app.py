from flask import Flask
from game_blueprint import game_blueprint

app = Flask(__name__)
app.register_blueprint(game_blueprint, url_prefix='/game')

if __name__ == '__main__':
    app.run(debug=True)