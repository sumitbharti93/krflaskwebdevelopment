from flask import Flask 

### WSGI application 
app = Flask(__name__) ## __name__ is passed as a parameter where the flask will look for resources , The flask object implements a WSGI application and acts as the central object 


@app.route('/') ## decorator helps in binding the function beneath the app.route 
def welcome():
    return "welcome to my web page, feeling good , now we are speaking "

@app.route('/members') ## decorator helps in binding the function beneath the app.route 
def member():
    return "New webpage "

print(__name__)
if __name__ == '__main__':
    app.run(debug = True )