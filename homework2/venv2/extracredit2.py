from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
	return "Hello Dummy"

@app.route("/add/<int:num1>/<int:num2>")
def addition(num1,num2):
	return str(num1+num2)

@app.route("/multiply/<num1>/<num2>")
def multiplication(num1,num2):
	result = int(num1)*int(num2)
	return str(result)

@app.route("/subtract/<num1>/<num2>")
def subtraction(num1,num2):
	return str(int(num1)-int(num2))

@app.route("/favoritefoods")
def fave():
	foodList = ["beef momos", "chilli paneer", "butter chicken"]
	return jsonify(foodList)