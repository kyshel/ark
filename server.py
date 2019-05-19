from flask import Flask, send_from_directory, request, jsonify
import json



app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def index():
	return send_static('index.html')   

@app.route('/do/',  defaults={'action': '1'}, methods=['GET','POST'])
@app.route('/do/<action>', methods=['GET','POST'])
def do(action):
	import ark_back
	ark_back.log(dir(request),0)
	res = {
	'status': 0,
	'time' : ark_back.get_time_now(),
	#'data': ark_back.do(action,dict(request.args)),
	'data': ark_back.do(action,request.args.to_dict()),
	}

	return jsonify(res)




@app.route('/<path:filename>')
def send_static(filename):
	return send_from_directory('static',
							   filename)





if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000,debug=True)