from flask import Flask,request

app = Flask(__name__)

@app.route('/users/<string:username>')
def hello_world(username=None):
    return("Hello {}!".format(username))

@app.errorhandler(400)
def custom400(error):
    response = jsonify({'message': error.description['message']})
    # etc.

@app.route('/predictrecord/<string:filename>')
def predictrecord(filename):
    '''
    if (filename.empty()):
       abort(400, {'message': 'custom error message to appear in body'})
    '''
    if (not filename):
        return('empty string')

    return(filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
