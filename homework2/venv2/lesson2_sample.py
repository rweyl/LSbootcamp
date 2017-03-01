from flask import Flask

app = Flask(__name__)

@app.route("/post/<postnum>")
def posts(postnum):
	return "This is post %s" % postnum
