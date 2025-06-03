from flask import Flask, render_template, request, flash, redirect, url_for
from models import buscar_ultimas_sessoes, salvar_materia

app = Flask(__name__)
app.secret_key = 'matheusandre'

@app.route('/inicial')
def inicial():
    ultimas_sessoes = buscar_ultimas_sessoes()
    return render_template('inicial.html', ultimas_sessoes=ultimas_sessoes)

@app.route('/criar_estudo', methods=['GET', 'POST'])
def criar_estudo():
    return render_template('criar_estudo.html')

@app.route('/criar_materia', methods=['GET', 'POST'])
def criar_materia():
    if request.method == 'POST':
        nome_materia = request.form.get('nome_materia')
        salvar_materia(nome_materia)
        flash('matéria cadastrada com sucesso!')
        return redirect(url_for('criar_estudo'))
    return render_template('criar_materia.html')

if __name__ == '__main__':
    app.run(debug=True)