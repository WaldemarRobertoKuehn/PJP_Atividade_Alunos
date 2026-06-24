"""
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def conectar():
    conexao = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_DATABASE")
    )
    return conexao

conexao = conectar()
online = conexao.is_connected()
if not online:
    print("Banco de dados não conectou!")
else:
    print("Banco de dados conectado!")
"""

"""
Conexão com o banco de dados MySQL usando variáveis de ambiente para configuração.
A função `conectar()` estabelece a conexão e retorna o objeto de conexão.
O script também verifica se a conexão foi bem-sucedida e imprime uma mensagem apropriada.
"""
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def conectar():
    host = os.getenv("DB_HOST")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    database = os.getenv("DB_DATABASE")

    if not (host and user and password and database):
        raise ValueError(
            "Faltam variáveis de ambiente: DB_HOST, DB_USER, DB_PASSWORD ou DB_DATABASE"
        )

    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        use_pure=True,
        connection_timeout=10,
    )


if __name__ == "__main__":
    conexao = conectar()
    try:
        if not conexao.is_connected():
            print("Banco de dados não conectou!")
        else:
            print("Banco de dados conectado!")
    finally:
        if conexao.is_connected():
            conexao.close()