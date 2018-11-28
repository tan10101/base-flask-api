from flask import Flask, Blueprint
from flask_restful import Api
from flask_moment import Moment
from config import config
from resources import *

moment = Moment()

def create_app(config_name):
  app = Flask(__name__)

  config_target = config[config_name]
  app.config.from_object(config_target)
  config_target.init_app(app)

  moment.init_app(app)

  api_bp = Blueprint('api', __name__, url_prefix='/api')
  api = Api(api_bp)

  api.add_resource(HomeResource, '/')

  app.register_blueprint(api_bp)
  return app

