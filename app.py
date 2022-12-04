import os
from flask import Flask
from flask_smorest import Api

from database import db
from resources.user import blp as UserBlueprint
from resources.category import blp as CategoryBlueprint
from resources.record import blp as RecordBlueprint


def create_app():
    app = Flask(__name__)

    basedir = os.path.abspath(os.path.dirname(__file__))

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'system.db')
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "SSDT|REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    db.init_app(app)

    api = Api(app)
    api.register_blueprint(UserBlueprint)
    api.register_blueprint(CategoryBlueprint)
    api.register_blueprint(RecordBlueprint)

    with app.app_context():
        db.create_all()

    return app


app = create_app()



