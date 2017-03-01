from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

connection = sqlite3.connect("sampledb_lesson3.db")
print("Opened database successfully")
connection.execute("CREATE TABLE IF NOT EXISTS posts (title TEXT, post TEXT)")
print("Table created successfully")
connection.close()

@app.route("/")
def index():
	return "Hello, World!"

@app.route("/new")
def new_post():
	return render_template("new_lesson3.html")

@app.route("/addrecord", methods=["POST"])
def addrecord():
	connection = sqlite3.connect("sampledb_lesson3.db")
	cursor = connection.cursor()

	try:
		title = request.form["title"]
		post = request.form["post"]
		print(title,post)
		cursor.execute("INSERT INTO posts (title,post) VALUES (?,?)", (title, post))
		connection.commit()
		message = "record successfully added"
	except:
		connection.rollback()
		message = "error in insert operation"
	finally:
		poop = message + title + post
		return render_template("result_lesson3.html", message=poop)
		# return message or return poop   either of these would also run instead of line 37
		connection.close()

# mylist = [1,2,3,4]
# mylist.append(5,6)
# mytuple = (1,2,3,4)
