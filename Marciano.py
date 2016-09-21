from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return "No hablo queso"

@app.route('/page2')
def goodbye_world():
	return "Hablo demasiado queso"

@app.route('/page3')
def rebirth():
	return "Ahora soy uno con el queso"

if __name__=="__main__":
    app.run()