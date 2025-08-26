from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Função de cálculo simples (baseada no que já foi discutido)
def calcular_dose(medicamento, idade, peso, conc_mg_ml, gtt_por_ml):
    # Aqui vai a lógica do cálculo com base no que já discutimos anteriormente
    return {
        "medicamento": medicamento,
        "idade": idade,
        "peso": peso,
        "conc_mg_ml": conc_mg_ml,
        "gtt_por_ml": gtt_por_ml,
        "resultado": f"Resultado calculado para {medicamento}."
    }

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.get_json()
    medicamento = data.get('medicamento')
    idade = data.get('idade')
    peso = data.get('peso')
    conc = data.get('conc')
    gttml = data.get('gttml')

    # Calcula a dose com base nas entradas
    resultado = calcular_dose(medicamento, idade, peso, conc, gttml)

    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)
