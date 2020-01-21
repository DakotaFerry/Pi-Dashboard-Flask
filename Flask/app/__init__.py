"""Initialize app."""
from flask import Flask


def create_app():
    """Construct the core application."""
    app_object = Flask(__name__,
                instance_relative_config=False)
    app_object.config.from_object('config.Config')

    with app_object.app_context():

        # Import main Blueprint
        from app import routes
        app_object.register_blueprint(routes.main_bp)

        return app_object