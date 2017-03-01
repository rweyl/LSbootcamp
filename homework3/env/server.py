from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("home.html")

@app.route("/enternew")
def enter_new():
	return render_template("food.html")

@app.route("/addfood", methods=["POST"])
def add_food():
	connection = sqlite3.connect("database.db")
	cursor = connection.cursor()

	try:
		name = request.form["name"]
		calories = request.form["calories"]
		cuisine = request.form["cuisine"]
		veggie = request.form["is_vegetarian"]
		gluten = request.form["is_gluten_free"]
		print(name,calories,cuisine,veggie,gluten)
		cursor.execute("INSERT INTO foods (name,calories,cuisine,is_vegetarian,is_gluten_free) VALUES (?,?,?,?,?)", (name,calories,cuisine,veggie,gluten))
		connection.commit()
		message = "records successfully added"
	except:
		connection.rollback()
		message = "error in insert operation"
	finally:
		return render_template("results.html", message=message)
		connection.close()

@app.route("/favorite")
def favorite():
	connection = sqlite3.connect("database.db")
	cursor = connection.cursor()
	
	cursor.execute("SELECT * FROM foods WHERE is_gluten_free='yes'")
	results = cursor.fetchall()
	return jsonify(results)
	connection.close()

@app.route("/search", methods=["GET"])
def search():
	connection = sqlite3.connect("database.db")
	cursor = connection.cursor()

	name = request.args.get("name") #or name = request.args["name"]
	cursor.execute("SELECT * FROM foods WHERE name=?", [name]) 
	results = cursor.fetchall()
	return jsonify(results)
	connection.close()

@app.route("/drop")
def drop():
	connection = sqlite3.connect("database.db")
	cursor = connection.cursor()

	cursor.execute("DROP TABLE foods")
	connection.commit()
	return "dropped"
	connection.close()

#in line 52, you either need [name] or (name,) so that your program recognizes it as mutable...treat as a list, not a tuple
#in line 51, since you're running a "get" query, you have 2 options to pass the parameter from your HTML
