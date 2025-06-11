from controller.ordenar import Ordenar
from flask import Flask, request, jsonify, render_template
app = Flask(__name__)
ordenar_controller = Ordenar()
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insertar', methods=['POST'])
def insertar():
    data = request.get_json()
    valor = float(data.get('valor'))
    if valor is not None:
        ordenar_controller.insertar(valor)
        return jsonify({'message': 'Valor insertado correctamente'}), 200
    else:
        return jsonify({'error': 'Valor no proporcionado'}), 400
    
@app.route('/ordenar', methods=['POST'])
def ordenar():
    ordenar_controller.ordenar()

@app.route('/mostrar_arbol', methods=['GET'])
def mostrar_arbol():
    arbol_json = ordenar_controller.obtener_arbol_como_json()
    return jsonify(arbol_json), 200

if __name__ == '__main__':
    app.run(debug=True)