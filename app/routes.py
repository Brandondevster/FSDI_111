from flask import Flask             # From the flask module import the Flask class.


app = Flask(__name__)               # Instantiate the Flask clas into the app variable.
                                    # Variables that contain class instances are calles "objects".


@app.route("/")                     # This is a decorator.
def index():                        # This is a function; In the context of flask it is a "view fucntion"
                                    # Return statement; This is returning a string.
    return "<h1>Hello, world!</h1>"


@app.get("/home")
def home():
    return "You're home!"


@app.route("/about", methods=["GET"])
def about():
    return "Hi, my name is Brandon Webster."


# def wrapper(other_function):
#     do stuff here
#     out = other_function()
#     do other stuff here
#     return out
