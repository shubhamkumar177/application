from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Backend URL
backend_url = 'http://13.233.88.51:9090/sum'  # Change to your backend URL

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])

    # Send the data to the backend server
    response = requests.get(backend_url, params={'num1': num1, 'num2': num2})

    if response.status_code == 200:
        result = response.json()['result']
        return render_template('index.html', result=result)
    else:
        return 'Error occurred while communicating with the backend server.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
