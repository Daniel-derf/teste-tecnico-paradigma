IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'TesteDB')
BEGIN
    CREATE DATABASE TesteDB;
END
GO

USE TesteDB;
GO

IF OBJECT_ID('Departamento', 'U') IS NOT NULL
    DROP TABLE Pessoa;
IF OBJECT_ID('Departamento', 'U') IS NOT NULL
    DROP TABLE Departamento;
GO

CREATE TABLE Departamento (
    Id INT PRIMARY KEY,
    Nome NVARCHAR(100) NOT NULL
);
GO

CREATE TABLE Pessoa (
    Id INT PRIMARY KEY,
    Nome NVARCHAR(100) NOT NULL,
    Salario DECIMAL(10, 2) NOT NULL,
    DeptId INT,
    FOREIGN KEY (DeptId) REFERENCES Departamento(Id)
);
GO

INSERT INTO Departamento (Id, Nome) VALUES (1, 'TI');
INSERT INTO Departamento (Id, Nome) VALUES (2, 'Vendas');
GO

INSERT INTO Pessoa (Id, Nome, Salario, DeptId) VALUES (1, 'Joe', 70000, 1);
INSERT INTO Pessoa (Id, Nome, Salario, DeptId) VALUES (2, 'Henry', 80000, 2);
INSERT INTO Pessoa (Id, Nome, Salario, DeptId) VALUES (3, 'Sam', 60000, 2);
INSERT INTO Pessoa (Id, Nome, Salario, DeptId) VALUES (4, 'Max', 90000, 1);
GO
