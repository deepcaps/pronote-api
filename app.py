from flask import Flask, json, request, render_template, jsonify
from get_elements import get_elements


app = Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/student_moyenne')
# http://<server_ip>/student_moyenne?username=<username>&password=<password>&link=<link>
def student_moyenne():
	username = request.args.get('username', default=None, type=str)
	password = request.args.get('password', default=None, type=str)
	link = request.args.get('link', default=None, type=str)

	moyenne = get_elements.student_moyenne(username, password, link)

	return jsonify(
		student_moyenne=moyenne
		)

@app.route('/classroom_moyenne')
# http://<server_ip>/classroom_moyenne?username=<username>&password=<password>&link=<link>
def classroom_moyenne():
	username = request.args.get('username', default=None, type=str)
	password = request.args.get('password', default=None, type=str)
	link = request.args.get('link', default=None, type=str)

	moyenne = get_elements.classroom_moyenne(username, password, link)

	return jsonify(
		classroom_moyenne=moyenne
		)

@app.route('/matter_moyenne')
# http://<server_ip>/matter_moyenne?username=<username>&password=<password>&link=<link>
def matter_moyenne():
	username = request.args.get('username', default=None, type=str)
	password = request.args.get('password', default=None, type=str)
	link = request.args.get('link', default=None, type=str)

	notes = get_elements.matter_moyenne(username, password, link)

	return jsonify(notes)


if __name__ == "__main__":
	app.run()