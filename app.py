from flask import Flask, jsonify, request, render_template
from quicktry import quicktry
import os

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    unedited_list = quicktry.query_images()
    option_list=[]
    for val in unedited_list:
        first = val.index('-')+1
        end = val.index(':')
        val=val[first:end]
        option_list.append(val)

    return render_template('index.html', option_list=option_list)


@app.route('/run', methods=['GET', 'POST'])
def run():
    """ Expects a json dictionary that specifies the language, code snippet, any
    expected input for the snippet. """
    content = request.get_json()
    if content is None:
        return jsonify({'status': -1, 'output': 'no input'})

    print(content)

    err, output = quicktry.execute(
            os.path.join(os.getcwd(), 'tmp'),
            content.get('code'),
            content.get('params'),
            content.get('lang').lower())

    print("error code {}\n{}".format(err, output))
    return jsonify({'status': err, 'output': output})


@app.route('/images')
def images():
    images = quicktry.query_images()
    return jsonify(images)

@app.route('/ajaxdata')
def ajaxdata():
    images = quicktry.query_images()
    imagesString= ""
    for val in images:
        option = "<option value='' id=''> val </option>"
        print (option)
        imagesString=imagesString + option
    return imagesString
