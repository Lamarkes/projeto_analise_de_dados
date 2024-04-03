from flask import *

import dao
import dataanalise as da
import pandas as pd

app = Flask(__name__)
dados = pd.read_csv('ProuniRelatorioDadosAbertos2020.csv', encoding='latin-1', delimiter=';', low_memory=False)
dados.drop(columns=['CODIGO_EMEC_IES_BOLSA'], axis=1, inplace=True)



@app.route('/graficobolsapormunicipio')
def analisarbolsapormunicipio():

    do = da.analisardadosbolsamunicipio(dados)
    figura = da.gerargraficobolsapormunicipio(do.head(20))

    return render_template('grafbolsapormunicipio.html', fig=figura.to_html())


@app.route('/graficocursoporuf')
def analisarcursosporuf():

    figura = da.gerargraficocursoporuf(dados.head(20))

    return render_template('grafcursoporuf.html', fig=figura.to_html())


@app.route('/graficoracapormunicipio')
def analisarracapormunicipio():

    do = da.analisardadosracapories(dados)
    figura = da.gerargraficoracapormunicipio(do.head(10))

    return render_template('grafbolsapormunicipio.html', fig=figura.to_html())

@app.route('/teste')
def analiseteste():
    pass


@app.route('/grafquantidadedecursospormunicipio')
def analisarqtdcursomunicipio():
    do = da.analisardadosmodalidadedeensino(dados)
    figura = da.gerargrafico(do.head(20))

    return render_template('grafcursospormunicipio.html',  fig=figura.to_html())

@app.route('/menu')
def menu():
    return render_template('menu.html')


@app.route('/')
def motormanda():
    return render_template('index.html')

@app.route('/cadastrarusuario', methods=['GET', 'POST'])
def redirecionar_cadastro_user():
    if request.method == 'GET':
        return render_template('cadastrarusuario.html')
    elif request.method == 'POST':
        login = str(request.form.get('nome'))
        senha = str(request.form.get('senha'))

        if dao.inseriruser(login, senha, dao.conectardb()):
            return render_template('index.html')
        else:
            texto= 'e-mail já cadastrado'
            return render_template('cadastrarusuario.html', msg=texto)

@app.route('/login', methods=['POST'])
def cadastrar_usuario():
    nome = str(request.form.get('nome'))
    senha = str(request.form.get('senha'))
    if (dao.verifcar_login(nome, senha, dao.conectardb())):
        return render_template('menu.html')
    else:
        return render_template('index.html')


@app.route('/salvarcorrelacaobd', methods=['POST'])
def salvarcorrelacao():
    ind1 = request.form.get('ind1')
    ind2 = request.form.get('ind2')
    correlacao = request.form.get('valorcorrelacao')

    if dao.insert_correlacao(dao.conectardb(), ind1, ind2, correlacao):
        return render_template('paginasucesso.html')
    else:
        return render_template('paginaerro.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
