def separador_titulo():
    print('-----TABELA-----')
    print('*' * 10)
    print('+' * 10)
    print('*' * 10)


def contagem_lihas_telefone():
    """
    :return: retorna a quantidade de linhas em tb_telefone.txt
    """
    with open('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/tb_telefone.txt', 'r', encoding='utf8') as r_telefone:
        linhas_telefone = 0
        arquivo_telefone = r_telefone.read().split("\n")
        for i in arquivo_telefone:
            if i:
                linhas_telefone += 1
    return linhas_telefone


# leitura de linhas do arquivo tb_endereco.txt
def contagem_lihas_endereco():
    """
        :return: retorna a quantidade de linhas em tb_endereco.txt
    """
    with open('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/tb_endereco.txt', 'r', encoding='utf-8') as r_endereco:
        linhas_endereco = 0
        arquivo_endereco = r_endereco.read().split("\n")
        for i in arquivo_endereco:
            if i:
                linhas_endereco += 1
    return linhas_endereco
