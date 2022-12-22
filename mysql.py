#   BIBLIOTECAS
from faker import Faker
from random import choice
import shutil


"""
1- buscar os registros aleatorio com a biblioteca faker
2- Criar colunas para primeiro nome, sobrenome, sexo, estado no MYSQL
3- separar nome e sobrenome pelo seus sexo
4- criar um loop até a quantidade desejada
5- A cada dado de cliente gerado, ele será escrito em um arquivo txt
6- O arquivo e movido para a pasta que o MYSQl permite a inserção
7- A leitura deste arquivo será feito pelo MYSQL com 'load data infile

    TRATAMENTOS A SEREM FEITOS

"""

f = Faker('pt_BR')
genero = ['M', 'F']
quantidade = 10

for cadastro in range(quantidade):
    # carregamento de cada cadastro conforme a quantidade desejada
    with open('cliente.txt', 'a', encoding='utf-8') as arquivo:
        # add dados em utf-8 para o arq.txt
        sexo = choice(genero)
        estado = f.estado_nome()
        match sexo:
            case 'M':
                # caso o sexo seja masculino, o nome e o sobrenome também será
                primeiro_nome = f.first_name_male()
                sobrenome = f.last_name_male()
            case 'F':
                # caso o sexo seja feminino, o nome e o sobrenome também será
                primeiro_nome = f.first_name_female()
                sobrenome = f.last_name_female()

        arquivo.writelines(f'{primeiro_nome},{sobrenome},{sexo},{estado}\n')
        print(F'{cadastro} com sucesso!')

# Arquivo movido para o diretorio com permissão do mysql
shutil.move('C:/Users/mathe/PycharmProjects/banco de dados/cliente.txt',
            'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads')
