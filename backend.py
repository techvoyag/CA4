from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace this with your Node.js backend URL
NODE_BACKEND_URL = "http://localhost:9002"


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = {
        'email': request.form['email'],
        'password': request.form['password']
    }
    response = requests.post(f'{NODE_BACKEND_URL}/login', data=data)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        # Handle the error, return an appropriate response
        return jsonify({'error': 'Login failed'}), 500  # 500 is the HTTP status code for Internal Server Error
    

@app.route('/register', methods=['POST'])
def register():
    data = {
        'name': request.form['name'],
        'email': request.form['email'],
        'password': request.form['password']
    }
    response = requests.post(f'{NODE_BACKEND_URL}/register', data=data)
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        # Handle the error, return an appropriate response
        return jsonify({'error': 'Login failed'}), 500  # 500 is the HTTP status code for Internal Server Error
    

if __name__ == '__main__':
    app.run(port=5000)  # Flask app running on port 5000
