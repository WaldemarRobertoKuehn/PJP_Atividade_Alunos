from conexao import conectar

class Aluno:
    def __init__(self, nome_aluno, media_aluno, id_aluno=None):                 
        self.id = id_aluno
        self.nome = nome_aluno
        self.media = media_aluno


    def exibir(self):
        texto = f"""
        Código: {self.id_aluno}
        Nome: {self.nome_aluno}
        Média: {self.media_aluno}
        """
        print(texto)

    def salvar(self):
        conexao = conectar()
        cursor = conexao.cursor()

        sql = "INSERT INTO aluno(id, nome, media)VALUES(%s, %s, %s)"
        cursor.execute(sql, (self.id, self.nome, self.media))

        conexao.commit()
        conexao.close()

def listar_alunos():
    conexao= conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM aluno" 
    cursor.execute(sql)

    alunos = []
    for id, nome, media in cursor.fetchall():
        aluno = Aluno(id, nome, media)
        alunos.append(aluno)

    conexao.close()
    return alunos