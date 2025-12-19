from . import game_blueprint
from flask import request

@game_blueprint.route('/join', methods=['POST'])
def hello():
    return request.json