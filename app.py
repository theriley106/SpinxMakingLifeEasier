from flask import Flask, render_template, request, url_for, redirect, Markup, jsonify, make_response, send_from_directory, session
import main

app = Flask(__name__, static_url_path='/static')
a = main.spinxAPI()

@app.route('/', methods=['GET'])
def index():
	storeInfo = a.DB()
	return render_template("index.html", storeInfo=storeInfo)

@app.route('/update', methods=['GET'])
def update():
	a.updateDatapoints()
	return jsonify(a.DB())



@app.route('/test', methods=['GET'])
def testPage():
	return render_template("index1.html")

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
