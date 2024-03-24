from os import name
from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse
import requests

app = Flask(__name__)
api = Api(app)

class VirtualMachine(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True)
        parser.add_argument('size', type=int, required=True)
        parser.add_argument('task', required=True)
        args = parser.parse_args()

        vm_id = args['id']
        size = args['size']
        task = args['task']

        # Проверка, что размер RAM является степенью двойки и в пределах допустимого значения
        if not (1 <= size <= 128 and (size & (size - 1) == 0)):
            return {"result": "NOT_OK"}, 400

        # Обращение к микросервису выбора сервера
        try:
            response = requests.post("http://server_selection_service:9025/find_best_fit", json={"size": size})
            response_data = response.json()
            if response.status_code == 200:
                server_id = response_data.get('server_id')
                return {"result": "OK", "host_id": server_id}
            else:
                return {"result": "NOT_OK"}, 400
        except requests.RequestException as e:
            return {"result": "NOT_OK"}, 500

api.add_resource(VirtualMachine, '/vm')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9024, debug=True)
