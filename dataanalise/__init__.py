import pandas as pd
import plotly.express as px


def analisardadosbolsamunicipio(dados):
    count_unicos = dados.groupby('MUNICIPIO_BENEFICIARIO')['TIPO_BOLSA'].nunique()
    count_unicos = pd.DataFrame(count_unicos)
    count_unicos.columns = ['counts']
    valor = dados['MUNICIPIO_BENEFICIARIO'].value_counts()
    return pd.DataFrame(valor)


def analisardadosracapories(dados):
    dados_modalidade_ensino = dados.groupby('RACA_BENEFICIARIO')['MUNICIPIO_BENEFICIARIO'].nunique()
    count_unicos = pd.DataFrame(dados_modalidade_ensino)
    count_unicos.columns = ['counts']
    valor_final = dados['MUNICIPIO_BENEFICIARIO'].value_counts()
    return pd.DataFrame(valor_final)


def analisardadosmodalidadedeensino(dados):
    count_unicos = dados.groupby('NOME_CURSO_BOLSA')['MUNICIPIO_BENEFICIARIO'].nunique()
    count_unicos = pd.DataFrame(count_unicos)
    count_unicos.columns = ['counts']
    valor = dados['NOME_CURSO_BOLSA'].value_counts()
    return pd.DataFrame(valor)
def gerargraficobolsapormunicipio(data):

    fig = px.bar(data, x=data.index, y='count')

    return fig


def gerargraficocursoporuf(data):
    fig = px.scatter(data, x='UF_BENEFICIARIO', y='NOME_CURSO_BOLSA')

    return fig

def gerargraficoracapormunicipio(data):

    fig = px.pie(data_frame=data, values='count', names=data.index)

    fig.update_layout(title='Quantidade de Raças Beneficiadas por Município')

    return fig


def gerargrafico(data):
    fig = px.bar(data, x=data.index, y='count', color="count", title="Long-Form Input")
    fig.update_layout(title='Quantidade de cursos por Município')
    return fig


def testegraf(data):
    pass

