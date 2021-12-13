from flask import Flask, request, jsonify

from .services import retrieve_orders, create_order

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api/orders/computers', methods=['GET', 'POST'])
def computers():
    if request.method == 'GET':
        return jsonify(retrieve_orders())
    elif request.method == 'POST':
        request_body = request.json
        return jsonify(create_order(request_body))
    else:
        raise Exception('Unsupported HTTP request type.')


if __name__ == '__main__':
    app.run()
