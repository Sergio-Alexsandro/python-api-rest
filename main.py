from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
db_path = 'alunos.db'  # Nome do arquivo do banco de dados SQLite


# Função para criar a tabela 'alunos' no banco de dados
def criar_tabela():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY,
        nome_aluno TEXT NOT NULL,
        nome_professor TEXT,
        idade INTEGER,
        nota_primeiro_semestre INTEGER,
        nota_segundo_semestre INTEGER
    )''')
    conn.commit()
    conn.close()


# Rota para criar um novo aluno (POST)
@app.route('/alunos/post', methods=['POST'])
def criar_aluno():
    data = request.json
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO alunos (nome_aluno, nome_professor, idade, nota_primeiro_semestre, nota_segundo_semestre) VALUES (?, ?, ?, ?, ?)",
        (data['nome_aluno'], data.get('nome_professor', None), data.get('idade', None),
         data.get('nota_primeiro_semestre', None), data.get('nota_segundo_semestre', None)))
    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Aluno criado com sucesso."}), 201


# Rota para listar todos os alunos (GET)
@app.route('/alunos/get', methods=['GET'])
def listar_alunos():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    conn.close()
    alunos_lista = []
    for aluno in alunos:
        aluno_dict = {
            "id": aluno[0],
            "nome_aluno": aluno[1],
            "nome_professor": aluno[2],
            "idade": aluno[3],
            "nota_primeiro_semestre": aluno[4],
            "nota_segundo_semestre": aluno[5]
        }
        alunos_lista.append(aluno_dict)
    return jsonify(alunos_lista)


# Rota para obter um aluno específico por ID (GET)
@app.route('/alunos/get/<int:aluno_id>', methods=['GET'])
def obter_aluno(aluno_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alunos WHERE id = ?", (aluno_id,))
    aluno = cursor.fetchone()
    conn.close()
    if aluno is None:
        return jsonify({"mensagem": f"Aluno com ID {aluno_id} não encontrado."}, 404)
    aluno_dict = {
        "id": aluno[0],
        "nome_aluno": aluno[1],
        "nome_professor": aluno[2],
        "idade": aluno[3],
        "nota_primeiro_semestre": aluno[4],
        "nota_segundo_semestre": aluno[5]
    }
    return jsonify(aluno_dict)


# Rota para atualizar um aluno por ID (PUT)
@app.route('/alunos/put/<int:aluno_id>', methods=['PUT'])
def atualizar_aluno(aluno_id):
    data = request.json
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE alunos SET nome_aluno=?, nome_professor=?, idade=?, nota_primeiro_semestre=?, nota_segundo_semestre=? WHERE id=?",
        (data.get('nome_aluno', None), data.get('nome_professor', None), data.get('idade', None),
         data.get('nota_primeiro_semestre', None), data.get('nota_segundo_semestre', None), aluno_id))
    conn.commit()
    conn.close()
    return jsonify({"mensagem": f"Aluno com ID {aluno_id} atualizado com sucesso."})


# Rota para excluir um aluno por ID (DELETE)
@app.route('/alunos/delete/<int:aluno_id>', methods=['DELETE'])
def excluir_aluno(aluno_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM alunos WHERE id=?", (aluno_id,))
    conn.commit()
    conn.close()
    return jsonify({"mensagem": f"Aluno com ID {aluno_id} excluído com sucesso."})


# Iniciar a aplicação
if __name__ == '__main__':
    criar_tabela()  # Certifique-se de criar a tabela antes de executar o aplicativo
    app.run(debug=True)
