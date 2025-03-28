from flask import Flask, request, jsonify;

import sqlite3 
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

print(app)

def mensagem1():
    return 'oi'

def mensagem2():
    return '<h2> Pagar as pessoas, faz bem as pessoas!!!</h2>'

@app.route("/pague") #end point
def exiba_mensagem():
    return mensagem2() + mensagem1()

@app.route("/caloteira")
def mensagem_do_calote():
    return '<h3>Pessoas que não pagam, é triste viu..</h3>'


def init_db():
    #Conecte o sqlite3 no arquvio database.db com a variável conn (connection)
    with sqlite3.connect("database.db") as conn:
        conn.execute("""
        create table if not exists livros(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            categoria TEXT NOT NULL,
            autor TEXT NOT NULL,
            image_url TEXT NOT NULL
        )
""")

init_db()

@app.route("/livrosdoados", methods=["GET"])
def listar_livros():
    with sqlite3.connect("database.db") as conn:
        livros = conn.execute("""select * from livros""").fetchall()
    
    livros_formatados = []

    for item in livros:
        dicionario_livros = {
            "id": item[0],
            "titulo": item[1],
            "categoria": item[2],
            "autor": item[3],
            "image_url": item[4]
        }
        livros_formatados.append(dicionario_livros)


    return jsonify(livros_formatados), 200

@app.route("/doar", methods=["POST"])
def doar():
    dados = request.get_json()

    titulo = dados.get("titulo")
    categoria = dados.get("categoria")
    autor = dados.get("autor")
    image_url = dados.get("image_url")
   
    if not titulo or not categoria or not autor or not image_url:
        return jsonify({"Erro":"Todos os campos são obrigatórios"}), 400
   
    with sqlite3.connect("database.db") as conn:
        conn.execute(f"""
        INSERT INTO livros (titulo, categoria, autor, image_url)
        VALUES ("{titulo}", "{categoria}", "{autor}", "{image_url}")
""")

    conn.commit() #salvar no banco

    return jsonify({"mensagem":"Livro Cadastrado com sucesso"}),201


#app.run()

#se o app.py for o arquivo principal da API: 
#execute o app.run com o modo debug ativado
if __name__ == "__main__":
    app.run(debug=True)