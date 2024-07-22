# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    db.init_app(app)

    with app.app_context():
        db.create_all()  # Ensure that all tables are created

    from .routes import routes as routes_blueprint # type: ignore
    app.register_blueprint(routes_blueprint)

    return app
