# Put your app in here.
from flask import Flask, request
from operations import add

app = Flask(__name__)

@app.get("/add")
def addition():
    a = request.args["a"]
    b = request.args["b"]
    int_a = int(a)
    int_b = int(b)
    return add(int_a,int_b)