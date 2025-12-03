CREATE DATABASE IF NOT EXISTS `mercadinho`;
USE `mercadinho`;

CREATE TABLE IF NOT EXISTS `Funcionario` (
  `idFuncionario` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NOT NULL,
  `CPF` VARCHAR(45) NOT NULL,
  `Endereco` VARCHAR(45) NOT NULL,
  `Telefone` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idFuncionario`),
  UNIQUE INDEX `CPF_UNIQUE` (`CPF` ASC),
  UNIQUE INDEX `Endereco_UNIQUE` (`Endereco` ASC),
  UNIQUE INDEX `Telefone_UNIQUE` (`Telefone` ASC),
  UNIQUE INDEX `Nome_UNIQUE` (`Nome` ASC)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS `Cliente` (
  `idCliente` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NOT NULL,
  `CPF` VARCHAR(45) NOT NULL,
  `Telefone` VARCHAR(45),
  PRIMARY KEY (`idCliente`),
  UNIQUE INDEX `CPF_UNIQUE` (`CPF` ASC)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `Departamento` (
  `idDepartamento` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idDepartamento`),
  UNIQUE INDEX `Nome_UNIQUE` (`Nome` ASC)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS `Fornecedor` (
  `idFornecedor` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idFornecedor`),
  UNIQUE INDEX `Nome_UNIQUE` (`Nome` ASC)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS `Produto` (
  `idProduto` INT NOT NULL AUTO_INCREMENT,
  `Departamento_idDepartamento` INT NOT NULL,
  `Nome` VARCHAR(45) NOT NULL,
  `Preco` VARCHAR(45) NOT NULL,
  `Data` DATE NOT NULL,
  `Fornecedor_idFornecedor` INT NOT NULL,
  PRIMARY KEY (`idProduto`),
  INDEX `fk_Produto_Departamento_idx` (`Departamento_idDepartamento` ASC),
  INDEX `fk_Produto_Fornecedor_idx` (`Fornecedor_idFornecedor` ASC),
  CONSTRAINT `fk_Produto_Departamento`
    FOREIGN KEY (`Departamento_idDepartamento`)
    REFERENCES `Departamento` (`idDepartamento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Produto_Fornecedor`
    FOREIGN KEY (`Fornecedor_idFornecedor`)
    REFERENCES `Fornecedor` (`idFornecedor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `Venda` (
  `idVenda` INT NOT NULL AUTO_INCREMENT,
  `Funcionario_idFuncionario` INT NOT NULL,
  `Cliente_idCliente` INT NOT NULL,
  `Data` DATE NOT NULL,
  `Valor_total` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idVenda`),
  INDEX `fk_Venda_Funcionario_idx` (`Funcionario_idFuncionario` ASC),
  INDEX `fk_Venda_Cliente_idx` (`Cliente_idCliente` ASC),
  CONSTRAINT `fk_Venda_Funcionario`
    FOREIGN KEY (`Funcionario_idFuncionario`)
    REFERENCES `Funcionario` (`idFuncionario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Venda_Cliente`
    FOREIGN KEY (`Cliente_idCliente`)
    REFERENCES `Cliente` (`idCliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `Venda_has_Produto` (
  `Venda_idVenda` INT NOT NULL,
  `Produto_idProduto` INT NOT NULL,
  `Quantidades` INT NOT NULL,
  PRIMARY KEY (`Venda_idVenda`, `Produto_idProduto`),
  INDEX `fk_Venda_has_Produto_Venda_idx` (`Venda_idVenda` ASC),
  INDEX `fk_Venda_has_Produto_Produto_idx` (`Produto_idProduto` ASC),
  CONSTRAINT `fk_Venda_has_Produto_Venda`
    FOREIGN KEY (`Venda_idVenda`)
    REFERENCES `Venda` (`idVenda`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Venda_has_Produto_Produto`
    FOREIGN KEY (`Produto_idProduto`)
    REFERENCES `Produto` (`idProduto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NOT NULL,
  `senha` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `users` (`nome`, `senha`) VALUES ('admin', '123');