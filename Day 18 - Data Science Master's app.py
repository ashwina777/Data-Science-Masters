# flask is a protocol used to access function and it is language independent
from flask import Flask

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
#link after exe- https://white-carpenter-ccvoq.pwskills.app:5000/test_fun

if __name__=="__main__":
    app.run(host="0.0.0.0")
# after executing copy the URL which is lang independent
# copy only lab url e.g https://white-carpenter-ccvoq.pwskills.app:5000/ * add :5000 which is port number
# succesfully executed funtion using url

# after editing hello world 1 and hello world2
# to access hello world1 - use lab url :500 - port number then helloworld1
# link is -> https://white-carpenter-ccvoq.pwskills.app:5000/hello1
