from flask import Flask, jsonify, request
from quicktry import quicktry
import os

app = Flask(__name__)


@app.route('/')
def index():
    return 'suh'

@app.route('/run', methods=['GET', 'POST'])
def run():
    """ Expects a json dictionary that specifies the language, code snippet, any
    expected input for the snippet. """
    content = request.get_json()
    if content is None:
        return 'empty'

    print(content)

    results = quicktry.execute(
            os.path.join(os.getcwd(), 'tmp'),
            content['data'],
            None).decode()

    return jsonify(results)


@app.route('/images')
def images():
    images = quicktry.query_images()
    return jsonify(images)
