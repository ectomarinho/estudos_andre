import sqlite3

def buscar_ultimas_sessoes():
    conexao = sqlite3.connect('estudos.db')
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()

    cursor.execute('''
    SELECT sessoes.data, sessoes.duracao, sessoes.local, sessoes.observacoes, materias.materia
    FROM sessoes
    JOIN materias ON sessoes.materia_id = materias.id
    ORDER BY sessoes.data DESC
    LIMIT 3                   
''')
    
    resultados = cursor.fetchall()
    conexao.close()
    return resultados

def salvar_materia(nome_materia):
    conexao = sqlite3.connect('estudos.db')
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()

    cursor.execute('''
    INSERT INTO materias (materia)
    VALUES (?)
''', (nome_materia,))
    
    conexao.commit()
    conexao.close()