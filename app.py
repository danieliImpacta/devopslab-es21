from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Atividade concluída com sucesso uhuuuu"

if __name__ == '__main__':
    app.run(debug=True)