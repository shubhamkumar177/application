from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sum', methods=['GET'])
def sum_numbers():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = num1 + num2
        return jsonify({'result': result}), 200
    except ValueError:
        return jsonify({'error': 'Invalid input. Please provide valid numeric values for num1 and num2.'}), 400
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred: {}'.format(str(e))}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
