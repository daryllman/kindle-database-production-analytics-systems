from flask import Flask, render_template
from flask_cors import CORS, cross_origin

import requests


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


# For sample json response for Api 1
api1_response = requests.get('https://randomuser.me/api')
api1_content = api1_response.json()


# For sample json response for Api 2
# api2_response = requests.get('https://0.0.0.0:8000/reviews')
# api2_content = api2_response.json()


@app.route('/')
@cross_origin()
def home():
    # return render_template('index.html', name=name)
    return '''<h2>Flask Frontend Basic Template </h2>
                <p>If you see this, it is working ✅</p>
                <h3>Available endpoints to check other functionalities:</h3>
                <p>
                    <b>
                    /api1: 
                    </b>
                    Api request to a working endpoint hosted online https://randomuser.me/api
                </p>
                <p>
                    <b>
                    /api2: 
                    </b>
                    Api request to MySQL endpoint on local machine
                </p>
            '''


@app.route('/api1')
@cross_origin()
def api_1():
    # return render_template('index.html', name=name)
    return f'''<h2>Api1</h2>
                <h3>Api request to a working endpoint hosted online https://randomuser.me/api</h3>
                <p>You should see a json response below</p>
                {api1_content}
            '''


@app.route('/api2')
@cross_origin()
def api_2():
    # return render_template('index.html', name=name)
    return f'''<h2>Api1</h2>
                <h3>Api request to a working endpoint hosted online https://randomuser.me/api</h3>
                <p>You should see a json response below</p>
                s
            '''


if __name__ == "__main__":
    flask_port = 5000
    print(f"Running App on port {flask_port}")
    # app.run(host="0.0.0.0", port=flask_port)
    app.run(port=flask_port, debug=True)
