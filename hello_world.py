from flask import Flask
from os import environ

import functools

app= Flask(__name__)

@app.route("/")

@app.route("/jedi/<first>/<last>")
def jedi_name(first, last):
    html= """
        <h1>
            Your Jedi name is...
        </h1>
        <h2>
            {}{}
        </h2>
        <img src="https://images-na.ssl-images-amazon.com/images/I/41KWBtHfOjL._SX300_.jpg">
    """
    return html.format(first[:2].title(), last[:3])
    
@app.route("/hello/<name>")
def hello_person(name):
    html= """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten. Awww....
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())    
    
    
    
if __name__=="__main__":
    app.run(host=environ['IP'], port=int(environ['PORT']))