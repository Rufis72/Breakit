from flask import Blueprint

game_blueprint = Blueprint('game_blueprint', __name__)

from . import join