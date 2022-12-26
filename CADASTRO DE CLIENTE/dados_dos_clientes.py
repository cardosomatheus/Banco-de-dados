#   BIBLIOTECAS
from funcoes_clientes import separador_titulo, contagem_lihas_telefone, contagem_lihas_endereco
from faker import Faker
from random import choice
from random import randint

f = Faker('pt_BR')
quantidade = int(input('informe a quantidadde de registros a ser criado: '))

# Todos os arquivos foram criado no diretorio que tem a permissão do mysql
separador_titulo()
for cadastro in range(quantidade):
    with open('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/tb_telefone.txt', 'a+', encoding='utf-8') as arq_telefone:
        # Cada variavel recebera um valor aleatorio em cada loop e sera adiconada ao arq_telefone
        tipo_tel = choice(['CEL', 'COM'])
        telefone = f.msisdn()
        ddd_tel = telefone[2:4]
        num_tel = telefone[4:]

        match tipo_tel:
            # Desta forma os numero não se repetiram e serão inseridos no tabela
            case 'CEL':
                # escrevendo o telefone no tb_telefone.txt se o tipo for 'CEL'
                if ddd_tel and num_tel not in arq_telefone:
                    arq_telefone.writelines(f'{tipo_tel},{ddd_tel},{num_tel}\n')
            case 'COM':
                # escrevendo o telefone no tb_telefone.txt se o tipo for 'COM'
                if ddd_tel and num_tel not in arq_telefone:
                    arq_telefone.writelines(f'{tipo_tel},{ddd_tel},{num_tel}\n')
    print(f'Registro {tipo_tel}, {ddd_tel}, {num_tel} salvo com sucesso em arq_telefone!')

separador_titulo()
for cadastro in range(quantidade):
    with open('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/tb_endereco.txt', 'a+', encoding='utf-8') as arq_endereco:
        estado = f.estado()
        uf = estado[0]
        nome_estado = estado[1]
        cidade = f.city()
        bairro = f.bairro()
        rua = f.street_name()
        num_casa = f.building_number()

        arq_endereco.writelines(f'{nome_estado},{uf},{cidade},{bairro},{rua},{num_casa}\n')
    print(f'Registro {nome_estado},{uf},{cidade},{bairro},{rua},{num_casa} salvo em  arquivo arq_endereco!')

separador_titulo()
for cadastro in range(quantidade):
    # carregamento de cada cadastro conforme a quantidade desejada
    with open('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/tb_cliente.txt', 'a+', encoding='utf-8') as arq_cliente:
        # add dados em utf-8 para o arq.txt
        genero = choice(['M', 'F'])
        estado = f.estado_nome()
        cpf = f.cpf()
        match genero:
            case 'M':
                # caso o sexo seja masculino, o nome e o sobrenome também será
                primeiro_nome = f.first_name_male()
                sobrenome = f.last_name_male()
            case 'F':
                # caso o sexo seja feminino, o nome e o sobrenome também será
                primeiro_nome = f.first_name_female()
                sobrenome = f.last_name_female()
        if cpf not in arq_cliente:
            arq_cliente.writelines(f'{primeiro_nome},{sobrenome},{genero},'
                                   f'{cpf},{randint(1, contagem_lihas_endereco())},'
                                   f'{randint(1, contagem_lihas_telefone())}\n')

        print(f'Registro {primeiro_nome},{sobrenome},{genero} salvo com sucesso em arq_cliente!')


