from controller.logica import Familia
from flask import Flask, jsonify, request, render_template
app = Flask(__name__)
familia = Familia()
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agregar_pessoa', methods=['POST'])
def agregar_pessoa():
    data = request.get_json()
    persona = data.get('persona')
    if not persona :
        return jsonify({'error': 'Datos incompletos'}), 400
    else:
        familia.adicionar_persnoa(persona)
        return jsonify({'message': 'Persona agregada con éxito'}), 201

@app.route('/agregar_relacionamento', methods=['POST'])
def agregar_relacionamento():
    data = request.get_json()
    persona1 = data.get('persona1')
    persona2 = data.get('persona2')
    if not persona1  or not persona2 :
        return jsonify({'error': 'Datos incompletos'}), 400
    else:
        familia.adicionar_relacionamiento(persona1, persona2)
        return jsonify({'message': 'Relacionamento agregado con éxito'}), 201

@app.route('/ver_arbol', methods=['GET'])
def ver_arbol():
    pessoas = familia.obtener_personas()
    relacionamentos = familia.obter_relacionamentos()
    return jsonify({
        'pessoas': pessoas,
        'relacionamentos': relacionamentos
    }), 200

@app.route('/ver_arbol_jerarquico', methods=['GET'])
def ver_arbol_jerarquico():
    arbol = familia.obtener_arbol_completo()
    return jsonify(arbol), 200


if __name__ == '__main__':
    app.run(debug=True)