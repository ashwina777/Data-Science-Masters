# flask is a protocol used to access function and it is language independent
from flask import Flask
from flask import request

app = Flask(__name__) # obj of flask - app

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/hello1")
def hello_world1():
    return "Hello, World1!"

@app.route("/hello2")
def hello_world2():
    return "Hello, World2!"

@app.route('/test_fun')
def test():
    a=5+6
    return "this is my first fun in flask {}".format(a)

@app.route('/input_url')
def request_input():
    data = request.args.get('x')
    return "this is my input fro url {}".format(data)
# apply ? at last and pass value to parameter 
# link is https://white-carpenter-ccvoq.pwskills.app:5000/input_url?x=ashwina
# OUTPUT: this is my input fro url ashwina
if __name__=="__main__":
    app.run(host="0.0.0.0")
