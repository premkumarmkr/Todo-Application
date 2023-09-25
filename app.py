from flask import Flask
import requests
# If `entrypoint` is not defined in app.yaml, GKE will look for an app
# called `app` in `main.py`.
app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    """Return the data from our nginx deployed server"""
	return "Welcome to Premkumar World"
if __name__ == '__main__':
    # We will now run our application
    app.run(host='localhost', port=8080, debug=True)
