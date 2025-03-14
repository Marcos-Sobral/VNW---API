from flask import Flask, request;

import sqlite3 

app = Flask(__name__)

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
    #Conecte o sqlite3 no arquvio banco_dados.db com a variável conn (connection)
    with sqlite3.connect("banco_dados.db") as conn:
        conn.execute("""
        create table if not exists livros(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            categoria TEXT NOT NULL,
            autor TEXT NOT NULL,
            imagem_url TEXT NOT NULL
        )
""")

init_db()

@app.route("/doar", methods=["POST"])

def doar():
    dados = request.get_json()

#app.run()

#se o app.py for o arquivo principal da API: 
#execute o app.run com o modo debug ativado
if __name__ == "__main__":
    app.run(debug=True)