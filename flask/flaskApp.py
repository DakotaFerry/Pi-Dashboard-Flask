#Making this app because uwsgi is killing me

from flask import Flask
from app import create_app
app = Flask(__name__)

def main():
    app = create_app()
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', debug=True)

if __name__ == "__main__":
    main()