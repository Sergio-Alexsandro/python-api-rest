from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configuração da conexão com o banco de dados
db = mysql.connector.connect(
    host='localhost',
    user='Admin',
    password='1Z4a7q2x',
    database='api_rest',
)
cursor = db.cursor()


# Rota para criar um novo aluno
@app.route('/alunos/post', methods=['POST'])
def criar_aluno():
    dados_aluno = request.json
    nome_aluno = dados_aluno['nome_aluno']
    nome_professor = dados_aluno.get('nome_professor', None)
    idade = dados_aluno.get('idade', None)
    nota_primeiro_semestre = dados_aluno.get('nota_primeiro_semestre', None)
    nota_segundo_semestre = dados_aluno.get('nota_segundo_semestre', None)

    # Insere o aluno no banco de dados
    cursor.execute(
        "INSERT INTO alunos (nome_aluno, nome_professor, idade, nota_primeiro_semestre, nota_segundo_semestre) VALUES (%s, %s, %s, %s, %s)",
        (nome_aluno, nome_professor, idade, nota_primeiro_semestre, nota_segundo_semestre))
    db.commit()

    return jsonify({"mensagem": "Aluno criado com sucesso."}), 201


# Rota para listar todos os alunos
@app.route('/alunos/get', methods=['GET'])
def listar_alunos():
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()

    alunos_lista = []
    for aluno in alunos:
        aluno_dict = {
            "id": aluno[0],
            "nome_aluno": aluno[1],
            "nome_professor": aluno[2],
            "idade": aluno[3],
            "nota_primeiro_semestre": float(aluno[4]) if aluno[4] is not None else None,
            "nota_segundo_semestre": float(aluno[5]) if aluno[5] is not None else None
        }
        alunos_lista.append(aluno_dict)

    return jsonify(alunos_lista)


# Rota para atualizar um aluno por ID
@app.route('/alunos/put/<int:aluno_id>', methods=['PUT'])
def atualizar_aluno(aluno_id):
    dados_aluno = request.json

    cursor.execute("SELECT * FROM alunos WHERE id = %s", (aluno_id,))
    aluno = cursor.fetchone()

    if not aluno:
        return jsonify({"mensagem": f"Aluno com ID {aluno_id} não encontrado."}, 404)

    nome_aluno = dados_aluno.get('nome_aluno', aluno[1])
    nome_professor = dados_aluno.get('nome_professor', aluno[2])
    idade = dados_aluno.get('idade', aluno[3])
    nota_primeiro_semestre = dados_aluno.get('nota_primeiro_semestre', aluno[4])
    nota_segundo_semestre = dados_aluno.get('nota_segundo_semestre', aluno[5])

    cursor.execute(
        "UPDATE alunos SET nome_aluno = %s, nome_professor = %s, idade = %s, nota_primeiro_semestre = %s, nota_segundo_semestre = %s WHERE id = %s",
        (nome_aluno, nome_professor, idade, nota_primeiro_semestre, nota_segundo_semestre, aluno_id))
    db.commit()

    return jsonify({"mensagem": f"Aluno com ID {aluno_id} atualizado com sucesso."})


# Rota para excluir um aluno por ID
@app.route('/alunos/delete/<int:aluno_id>', methods=['DELETE'])
def excluir_aluno(aluno_id):
    cursor.execute("SELECT * FROM alunos WHERE id = %s", (aluno_id,))
    aluno = cursor.fetchone()

    if not aluno:
        return jsonify({"mensagem": f"Aluno com ID {aluno_id} não encontrado."}, 404)

    cursor.execute("DELETE FROM alunos WHERE id = %s", (aluno_id,))
    db.commit()

    return jsonify({"mensagem": f"Aluno com ID {aluno_id} excluído com sucesso."})


if __name__ == '__main__':
    app.run(debug=True)
