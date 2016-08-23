from quicktry import app, sandbox
from flask import jsonify, request, render_template
import os
import yaml

@app.route('/')
def index():
    unedited_list = sandbox.query_images()
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

    err, output = sandbox.execute(
            content.get('lang').lower(),
            content.get('code'),
            content.get('params'),
            os.path.join(os.getcwd(), 'tmp'))

    print("error code {}\n{}".format(err, output))
    return jsonify({'status': err, 'output': output})


@app.route('/images')
def images():
    return jsonify(sandbox.query_images())


@app.route('/languages')
def languages():
    return jsonify(sandbox.get_languages())


@app.route('/ajaxdata')
def ajaxdata():
    language = request.args.get('language')
    code = request.args.get('code')

    err, output = sandbox.execute(
            language,
            code,
            None,
            os.path.join(os.getcwd(), 'tmp'))

    #print("error code {}\n{}".format(err, output))
    #return jsonify({'status': err, 'output': output})
    return jsonify(result=output)

