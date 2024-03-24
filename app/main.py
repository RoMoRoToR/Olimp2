from os import name

from flask import Flask, request, jsonify

app = Flask(__name__)

servers = {i: 128 for i in range(1, 1001)}  # Пример инициализации серверов


@app.route('/find_best_fit', methods=['POST'])
def find_best_fit():
    size = request.json.get('size')
    best_fit = None
    min_ram_left = float('inf')
    for server_id, available_ram in servers.items():
        if available_ram >= size and (available_ram - size) < min_ram_left:
            best_fit = server_id
            min_ram_left = available_ram - size
    if best_fit is not None:
        servers[best_fit] -= size  # Уменьшаем доступную память
        return jsonify({"server_id": best_fit})
    else:
        return jsonify({"error": "No available server"}), 404


if name == '__main__':
    app.run(host='0.0.0.0', port=9025, debug=True)