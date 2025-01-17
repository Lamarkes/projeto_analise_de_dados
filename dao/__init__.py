import psycopg2

def conectardb():
    conn = psycopg2.connect(
        host='localhost',
        database='aplicacaoanalisedados',
        user='postgres',
        password='pgroot'
    )

    return conn


def verifcar_login(nome, senha, conexao):

    cur = conexao.cursor()
    cur.execute(f"SELECT count(*) FROM usuarios WHERE login = '{nome}' AND senha = '{senha}'")
    recset = cur.fetchall()
    conexao.close()
    if recset[0][0] == 1:
        return True
    else:
        return False


def insert_correlacao(conexao, ind1,ind2, valor):
    cur = conexao.cursor()
    exito = False
    try:
        #mudar nome da tabela
        sql = f"INSERT INTO resultadoanalise (indicador1, indicador2, valor) VALUES ('{ind1}', '{ind2}', '{valor}' )"
        cur.execute(sql)
    except psycopg2.IntegrityError:
        conexao.rollback()
        exito = False
    else:
        conexao.commit()
        exito = True

    conexao.close()
    return exito

def inseriruser(login, senha, conexao):
    cur = conexao.cursor()
    exito = False
    try:
        sql = f"INSERT INTO usuarios (login, senha) VALUES ('{login}', '{senha}' )"
        cur.execute(sql)
    except psycopg2.IntegrityError:
        conexao.rollback()
        exito = False
    else:
        conexao.commit()
        exito = True

    conexao.close()
    return exito



def listarUsuarios(conexao):
    cur = conexao.cursor()
    cur.execute('select * from usuarios')
    recset = cur.fetchall()
    conexao.close()

    return recset