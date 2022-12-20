# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, jsonify

app = Flask(__name__)

# フィボナッチ数を返す関数


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


@app.route('/fib', methods=['GET'])
def handle_request():
    n = request.args.get('n')
    try:
        result = fibonacci(int(n))
    except:
        return jsonify({"status": 400, "message": "Bad request."}), 400
    return jsonify({"result": result}), 200
