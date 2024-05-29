from flask import Flask


def create_app():
    app = Flask(__name__)

    with app.app_context():
        from .controllers import sentiment_bp
        app.register_blueprint(sentiment_bp)

    return app
