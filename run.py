from flask import Flask, render_template, request
from flask_restful import Resource, Api
from main import app

from com_blacktensor.cop.emo.resource.emotion import Emotion
app.run(host='192.168.0.10', port='8080', debug=True)
# app.run(host='127.0.0.1', port='8080', debug=True)
# '''
# app = Flask(__name__)
# api = Api(app)
# @app.route('/')
# def main_get(num=None):
#     return render_template(num=num)
# if __name__ == "__main__":
#     app.run(host='192.168.0.10', port='8080', debug=True)
    # return render_template('####.html', num=num)

# @app.route('/api/emotion', method = ['GET', 'POST'])
# def stock_name():
#     if request.method == 'GET':
#         keyword = request.args.get('keyword')
#         print(request.form)

#     # return render_template('.jsx', keyword = keyword)
#     return render_template(keyword = keyword)
#     # return 0
# if __name__ == "__main__":
#     app.run(host='192.168.0.10', port='8080', debug=True)
# '''
'''
@app.route('/api/emotion', method = ['POST', 'GET'])
def stock_name(num=None):
    if request.method == 'POST':
        # temp = request.form['num']
        pass
    elif request.method == 'GET':
        temp = request.args.get('num')
        # temp = str(temp)
        temp1 = request.args.get('keyword')
        print('Ok!')
        # return render_template('####.html', num=temp, keyword=temp1)

if __name__ == '__main__':
  app.run(host='192.168.0.10', port='8080', debug=True)  
'''

'''
app = Flask(__name__)
api = Api(app)
 
class Rest(Resource):
    def get(self):
        return {'rest': '한국 !'}
        # return Emotion()
    def post(self):
        return {'rest': 'post success !'}
api.add_resource(Rest, '/api')
 
if __name__ == '__main__':
    app.run(host='192.168.0.10', port='8080', debug=True)
'''
'''
app = Flask(__name__)
api = Api(app)


@app.route('/test')
def test():
    if request.method == 'Post':
    return {'test' : 'test Success!'}
def get():
    return {'get' : 'get Success!'}
def post():
    return {'post' : 'post Success!'}

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)
'''

'''
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world!'

if __name__ == 'main':
    app.run(host='192.168.0.10', port='8080', debug=True)

'''