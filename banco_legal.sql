DROP DATABASE IF EXISTS mercadinho;
CREATE DATABASE mercadinho;
USE mercadinho;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL
);

INSERT INTO users (nome, senha) VALUES ("admin", "123");

CREATE TABLE produto (
    idProduto INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Categoria VARCHAR(100),
    Preco DECIMAL(10,2) NOT NULL,
    Quantidade INT NOT NULL DEFAULT 0
);

CREATE TABLE funcionario (
    idFuncionario INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    CPF VARCHAR(14) NOT NULL UNIQUE,
    Cargo VARCHAR(50),
    Endereco VARCHAR(200),
    Telefone VARCHAR(20)
);

CREATE TABLE fornecedor (
    idFornecedor INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(255) NOT NULL,
    Telefone VARCHAR(20),
    Endereco VARCHAR(255)
);

ALTER TABLE produto
ADD COLUMN idFornecedor INT,
ADD CONSTRAINT fk_produto_fornecedor
    FOREIGN KEY (idFornecedor)
    REFERENCES fornecedor(idFornecedor);

CREATE TABLE venda (
    idVenda INT AUTO_INCREMENT PRIMARY KEY,
    idProduto INT NOT NULL,
    Quantidade INT NOT NULL,
    PrecoTotal DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (idProduto) REFERENCES produto(idProduto)
);

ALTER TABLE venda
ADD COLUMN idFuncionario INT NOT NULL,
ADD CONSTRAINT fk_venda_funcionario
    FOREIGN KEY (idFuncionario)
    REFERENCES funcionario(idFuncionario);