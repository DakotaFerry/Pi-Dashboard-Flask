# Making this app because uwsgi is killing me
from flask import Flask


def create_app(environ, start_response):
    """Construct the core application."""
    app = Flask(__name__,
                instance_relative_config=False)
    app.config.from_object('config.Config')

    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)

    with app.app_context():
        # Import main Blueprint
        import routes
        app.register_blueprint(routes.main_bp)

        import assets
        assets.compile_assets(app)

        return app


def main():
    app = create_app()
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', debug=True)


if __name__ == "__main__":
    main()
