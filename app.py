from flask import Flask, render_template, request, url_for, redirect, Markup, jsonify, make_response, send_from_directory, session

app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=['GET'])
def index():
	price = {"Dollar": '1', "CentOne": '1', "CentTwo": '2'}
	store = {"Address": '4 address', "Price": 5.11, "Number": 2261}
	return render_template("index.html", store=store)

@app.route('/test', methods=['GET'])
def testPage():
	return render_template("index1.html")

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5000)
