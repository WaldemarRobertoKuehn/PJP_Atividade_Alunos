from conexao import conectar

class Aluno:
    def __init__(self, nome_aluno, media_aluno, id_aluno=None):                 
        self.id_aluno = id_aluno
        self.nome_aluno = nome_aluno
        self.media_aluno = media_aluno
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

        sql = "INSERT INTO aluno(nome_aluno, media_aluno) VALUES(%s, %s)"
        cursor.execute(sql, (self.nome_aluno, self.media_aluno))

        conexao.commit()
        cursor.close()
        conexao.close()

def listar_alunos():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM aluno"
    cursor.execute(sql)

    alunos = []
    for id_aluno, nome_aluno, media_aluno in cursor.fetchall():
        aluno = Aluno(nome_aluno, media_aluno, id_aluno)
        alunos.append(aluno)

    cursor.close()
    conexao.close()
    return alunos