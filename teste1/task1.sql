

USE TesteDB;
GO

SELECT 
    d.Nome AS Departamento,
    p.Nome AS Pessoa,
    p.Salario
FROM (
    SELECT 
        Nome,
        Salario,
        DeptId,
        RANK() OVER (PARTITION BY DeptId ORDER BY Salario DESC) AS Ranking
    FROM Pessoa
) AS p
INNER JOIN Departamento d ON p.DeptId = d.Id
WHERE p.Ranking = 1
ORDER BY d.Nome;

