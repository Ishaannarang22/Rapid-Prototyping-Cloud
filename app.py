import os
from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config['DEBUG'] = os.environ.get('FLASK_DEBUG')

@app.route("/")
def hello():
    return "Hello world"

@app.route("/api/data")
def example():
    return "hello world"

if __name__ == "__main__":
    app.run(debug=True)