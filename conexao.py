import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def conectar():
    conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="escola"  
    )
    return conexao

conexao = conectar()
online = conexao.is_connected()
if not online:
    print("Banco de dados não conectou!")
else:
    print("Banco de dados conectado!")