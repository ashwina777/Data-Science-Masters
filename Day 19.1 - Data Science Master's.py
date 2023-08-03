from flask import Flask,request ,render_template , jsonify

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/math',methods=['POST'])
def math_ops():
    if(request.method == 'POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if ops == 'add':
            r = num1+num2
            result = "The sum of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
        if ops == 'subtract':
            r = num1-num2
            result = "The subtract of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
        if ops == 'multiply':
            r = num1*num2
            result = "The multiply of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
        if ops == 'divide':
            r = num1/num2
            result = "The divide of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
            
        return render_template('results.html' , result = result)




@app.route('/postman_action',methods=['POST'])
def math_ops1():
    if(request.method == 'POST'):
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if ops == 'add':
            r = num1+num2
            result = "The sum of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
        if ops == 'subtract':
            r = num1-num2
            result = "The subtract of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
        if ops == 'multiply':
            r = num1*num2
            result = "The multiply of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
        if ops == 'divide':
            r = num1/num2
            result = "The divide of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
            
        return jsonify(result)

if __name__=="__main__":
    app.run(host="0.0.0.0")
"""
--- COMMANDS TO CLONE A GIT REPOSITORY---
abc@ee4a1a0126be:~/workspace$ ls
app.py  README.md  requirements.txt  static  templates
abc@ee4a1a0126be:~/workspace$ git init
Reinitialized existing Git repository in /config/workspace/.git/
abc@ee4a1a0126be:~/workspace$ git add .
abc@ee4a1a0126be:~/workspace$ git commit -m "this is my flask code"

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'abc@ee4a1a0126be.(none)')
abc@ee4a1a0126be:~/workspace$  git config --global user.email "ashwinarawat8@gmail.com"
abc@ee4a1a0126be:~/workspace$ git config --global user.name "ashwina777"
abc@ee4a1a0126be:~/workspace$ git branch -M main
abc@ee4a1a0126be:~/workspace$ git remote add origin https://github.com/ashwina777/flask_app.git
fatal: remote origin already exists.
abc@ee4a1a0126be:~/workspace$ git remote remove origin
abc@ee4a1a0126be:~/workspace$ git remote add origin https://github.com/ashwina777/flask_app.git
abc@ee4a1a0126be:~/workspace$ git push -u origin main
Enumerating objects: 63, done.
Counting objects: 100% (63/63), done.
Delta compression using up to 64 threads
Compressing objects: 100% (59/59), done.
Writing objects: 100% (63/63), 13.44 KiB | 2.24 MiB/s, done.
Total 63 (delta 15), reused 0 (delta 0)
remote: Resolving deltas: 100% (15/15), done.
To https://github.com/ashwina777/flask_app.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
abc@ee4a1a0126be:~/workspace$ 
"""