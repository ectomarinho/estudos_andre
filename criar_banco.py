import sqlite3

conexao = sqlite3.connect('estudos.db')
conexao.execute('PRAGMA foreign_keys = ON;')
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS materias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    materia TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS sessoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    materia_id INTEGER NOT NULL,
    resumo TEXT,
    duracao INTEGER,
    data DATE,
    local TEXT,
    observacoes TEXT,
    FOREIGN KEY (materia_id) REFERENCES materias(id)
)
''')

conexao.commit()
conexao.close()

print('banco de dados e tabelas criados com sucesso!')