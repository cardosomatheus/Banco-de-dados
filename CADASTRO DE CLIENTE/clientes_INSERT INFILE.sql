-- CRIAÇÃO E ESCOLHA DO DATABASE 
CREATE DATABASE USUARIO;
USE USUARIO;

-- CRIAÇÃO DA TABELA DE CLIENTES
CREATE TABLE TB_CLIENTE(
	IDCLIENTE INT PRIMARY KEY AUTO_INCREMENT,
	PRIMEIRO_NOME VARCHAR(30) NOT NULL,
    SOBRENOME VARCHAR(30) NOT NULL,    
	GENERO CHAR(1),
    CPF VARCHAR(14) UNIQUE,
    FKENDERECO INT,
    FKTELEFONE INT
);

-- CRIAÇÃO DA TABELA DE ENDERECOS
CREATE TABLE TB_ENDERECO(
	IDENDERECO INT PRIMARY KEY AUTO_INCREMENT,
	ESTADO VARCHAR(30) NOT NULL,
    UF CHAR(2),
    CIDADE VARCHAR(30),
    BAIRRO VARCHAR(30),
    RUA VARCHAR(30),
    NUMERO VARCHAR(5)
);

-- CRIAÇÃO DA TABELA DE TELEFONES
CREATE TABLE TB_TELEFONE(
	IDTELEFONE INT PRIMARY KEY AUTO_INCREMENT,
    TIPO ENUM('CEL','COM'),
    DDD CHAR(2),
	TELEFONE VARCHAR(9)
);

-- ADICIONANDO AS CONSTRAINT 
ALTER TABLE TB_CLIENTE ADD CONSTRAINT FK_CLIENTE_ENDERECO
FOREIGN KEY (FKENDERECO)
REFERENCES TB_ENDERECO(IDENDERECO);

ALTER TABLE TB_CLIENTE ADD CONSTRAINT FK_CLIENTE_TELEFONE
FOREIGN KEY (FKTELEFONE)
REFERENCES TB_TELEFONE(IDTELEFONE);


/*INSERTS ATRAVÉS DE UM ARQUIVO TXT 
1- PASSEI O CAMINHO DO ARQUIVO TXT
2- SELECIONEI A TABELA DE INSERÇÃO
3- INFORMEI O TERMINO DE CADA REGISTRO E O MODO DE CERCO
4- INFORMEI QUE CADA LINHA DE DADOS TEM UMA QUBRA \n
5- SELECIONEI OS CAMPOS QUE SERÃO PREENCHIDO PELOS DADOS NO TXT
*/

-- INSERÇÃO DOS DADOS DE CADA ARQUIVO NA TABELA TB_TELEFONE
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/tb_telefone.txt'
INTO TABLE TB_TELEFONE
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
(TIPO,DDD,TELEFONE);

-- INSERÇÃO DOS DADOS DE CADA ARQUIVO NA TABELA TB_ENDERECO
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/tb_endereco.txt'
INTO TABLE TB_ENDERECO
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
(ESTADO,UF,CIDADE,BAIRRO,RUA,NUMERO);

-- INSERÇÃO DOS DADOS DE CADA ARQUIVO NA TABELA TB_CLIENTE
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/tb_cliente.txt'
INTO TABLE TB_CLIENTE
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
(PRIMEIRO_NOME,SOBRENOME,GENERO,CPF,FKENDERECO,FKTELEFONE);





