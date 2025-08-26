from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Função de cálculo simples (baseada no que já foi discutido)
def calcular_dose(medicamento, idade, peso, conc_mg_ml, gtt_por_ml):
    # Aqui vai a lógica do cálculo com base no que já discutimos anteriormente
    resultado = {
        "medicamento": medicamento,
        "idade": idade,
        "peso": peso,
        "conc_mg_ml": conc_mg_ml,
        "gtt_por_ml": gtt_por_ml,
        "dose_mg": peso * 10,  # Exemplo de cálculo simples de dose
        "total_gotas": (peso * 10) / conc_mg_ml * gtt_por_ml  # Calcula as gotas
    }
    return resultado

# Rota para a página inicial (HTML)
@app.route('/')
def index():
    return app.send_static_file('index.html')  # Flask irá procurar o arquivo dentro da pasta 'static'

# Rota para o cálculo
@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.get_json()  # Obtém os dados enviados pelo frontend
    medicamento = data.get('medicamento')
    idade = data.get('idade')
    peso = data.get('peso')
    conc = data.get('conc')
    gttml = data.get('gttml')

    # Chama a função de cálculo com os dados recebidos
    resultado = calcular_dose(medicamento, idade, peso, conc, gttml)

    return jsonify(resultado)  # Retorna o resultado para o frontend

if __name__ == '__main__':
    app.run(debug=True)
