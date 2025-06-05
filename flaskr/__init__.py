import os
from flask import Flask

# ! Essa é a função fábrica da aplicação, serve pra lançar o servidor e já deixar toda sua configuração pronta.
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev', # ! Trocar aqui quando colocar em deploy!
        DATABASE = os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/teste')
    def teste():
        return '<p>Testando...</p>'
    
    return app