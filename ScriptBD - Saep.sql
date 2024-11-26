CREATE DATABASE saep;
USE saep;

CREATE TABLE User 
(
	ID INT NOT NULL PRIMARY KEY,
    Nome VARCHAR(45) NOT NULL,
    Email VARCHAR(45) NOT NULL
);


CREATE TABLE Tarefa 
(
	ID INT NOT NULL PRIMARY KEY, 
    IdUser INT NOT NULL, 
    Titulo VARCHAR(45),
    Descricao VARCHAR(100),
    Setor VARCHAR(45),
    Prioridade VARCHAR(45),
    DataCadastro DATETIME,
    Status varchar(45),
    
    FOREIGN KEY (IdUser) REFERENCES User(ID)
);

