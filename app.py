from flask import Flask, make_response, jsonify, request
from bd import Carros

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

def show_response(_message: str, _data:list[any], _per_page:int = 1):
    return jsonify(
            message = _message,
            data = _data,
            per_page = _per_page
        )

@app.route('/carros', methods=['GET'])
def index():
    return make_response(
        show_response("Listando todos os veículos.", Carros, len(Carros))
    )

@app.route('/carros', methods=['POST'])
def store():
    carro = request.json
    Carros.append(carro)
    return show_response("Veículo adicionado com sucesso!", [carro], len(Carros))

app.run()