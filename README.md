# Teste Técnico - Desafios de Programação

Este repositório contém a implementação de dois desafios técnicos.

## 📁 Estrutura do Projeto

```
teste-tecnico/
├── teste1/              # Desafio 1: SQL Server + Docker
│   ├── docker-compose.yml
│   ├── init.sql
│   ├── task1.sql
│   └── setup.sh
├── teste2/              # Desafio 2: Árvore Binária em Python
│   ├── tree_builder.py
│   ├── main.py
│   ├── test_tree_builder.py
│   ├── requirements.txt
│   └── venv/
└── README.md
```

---

## 🗄️ Teste 1: SQL Server - Query com Window Functions

### 📋 Descrição

Encontrar os colaboradores com o maior salário em cada departamento usando SQL Server.

### 🚀 Como Executar

#### Opção 1: Script Automático (Recomendado)

```bash
cd teste1
./setup.sh
```

#### Opção 2: Passo a Passo Manual

**1. Iniciar o SQL Server no Docker**

```bash
cd teste1
docker compose up -d
```

**2. Aguardar inicialização (30 segundos)**

```bash
sleep 30
```

**3. Criar banco de dados e tabelas**

```bash
docker exec -it sqlserver_teste /opt/mssql-tools18/bin/sqlcmd \
    -S localhost -U SA -P 'MyStrongPass123!' -C \
    -i /init.sql
```

**4. Executar a query da solução**

```bash
docker exec -it sqlserver_teste /opt/mssql-tools18/bin/sqlcmd \
    -S localhost -U SA -P 'MyStrongPass123!' -C \
    -i /task1.sql
```

#### Modo Interativo (SQL Manual)

```bash
docker exec -it sqlserver_teste /opt/mssql-tools18/bin/sqlcmd \
    -S localhost -U SA -P 'MyStrongPass123!' -C
```

Dentro do `sqlcmd`:

```sql
USE TesteDB;
GO

SELECT * FROM Departamento;
GO

SELECT * FROM Pessoa;
GO

-- Query da solução
SELECT d.Nome AS Departamento, p.Nome AS Pessoa, p.Salario
FROM (
    SELECT Nome, Salario, DeptId,
           RANK() OVER (PARTITION BY DeptId ORDER BY Salario DESC) AS Ranking
    FROM Pessoa
) AS p
INNER JOIN Departamento d ON p.DeptId = d.Id
WHERE p.Ranking = 1
ORDER BY d.Nome;
GO
```

### 📊 Resultado Esperado

```
Departamento  Pessoa  Salario
------------  ------  -------
TI            Max     90000.00
Vendas        Henry   80000.00
```

### 🔧 Conexão Externa

- **Host:** localhost
- **Port:** 1433
- **User:** SA
- **Password:** MyStrongPass123!
- **Database:** TesteDB

### 🛑 Parar o Ambiente

```bash
cd teste1
docker compose down
```

---

## 🌲 Teste 2: Árvore Binária em Python

### 📋 Descrição

Construir uma árvore binária a partir de um array, onde:

- **Raiz**: Maior valor do array
- **Esquerda**: Valores à esquerda da raiz
- **Direita**: Valores à direita da raiz

### 🚀 Como Executar

#### 1. Configurar Ambiente Virtual (primeira vez)

```bash
cd teste2

# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

#### 2. Executar Demonstração dos Cenários

```bash
# Ativar venv (se ainda não estiver ativo)
source venv/bin/activate

# Executar demonstração
python3 main.py
```

**Saída Esperada:**

```
============================================================
CENÁRIO 1
============================================================
Array de entrada: [3, 2, 1, 6, 0, 5]

Raiz: 6
Galhos da esquerda: [3, 2, 1]
Galhos da direita: [0, 5]

Árvore construída:
└── 6
    ├── 3
    │   └── 2
    │       └── 1
    └── 5
        ├── 0

============================================================
CENÁRIO 2
============================================================
Array de entrada: [7, 5, 13, 9, 1, 6, 4]

Raiz: 13
Galhos da esquerda: [7, 5]
Galhos da direita: [9, 1, 6, 4]

Árvore construída:
└── 13
    ├── 7
    │   └── 5
    └── 9
        └── 6
            ├── 1
            └── 4
```

#### 3. Executar Testes Unitários

```bash
# Ativar venv (se ainda não estiver ativo)
source venv/bin/activate

# Executar todos os testes (20 testes)
pytest test_tree_builder.py -v

# Executar com cobertura detalhada
pytest test_tree_builder.py -v --tb=short

# Executar teste específico
pytest test_tree_builder.py::TestTreeBuilder::test_cenario_1 -v
```

**Resultado Esperado:**

```
====================== test session starts ======================
collected 20 items

test_tree_builder.py::TestTreeBuilder::test_cenario_1 PASSED
test_tree_builder.py::TestTreeBuilder::test_cenario_2 PASSED
...
======================= 20 passed in 0.06s ======================
```

### 💻 Uso Programático

```python
from tree_builder import build_tree_from_array

# Criar árvore
arr = [3, 2, 1, 6, 0, 5]
tree = build_tree_from_array(arr)

# Visualizar
tree.print_tree()

# Obter percursos
print(tree.preorder())  # [6, 3, 2, 1, 5, 0]
print(tree.inorder())   # [3, 2, 1, 6, 0, 5]

# Obter estrutura
print(tree.get_structure())
```

### 🧪 Cobertura de Testes

- ✅ **2 cenários do desafio**
- ✅ **Arrays de tamanhos variados** (1 a 20 elementos)
- ✅ **Posições da raiz** (início, meio, fim)
- ✅ **Valores especiais** (negativos, zero)
- ✅ **Arrays ordenados** (crescente, decrescente)
- ✅ **Validações** (array vazio, duplicatas)
- ✅ **Estrutura da árvore** (nós, percursos)

**Total: 20 testes** 🎯

### 🛑 Desativar Ambiente Virtual

```bash
deactivate
```

---

## ⚙️ Requisitos do Sistema

### Teste 1 (SQL)

- Docker
- Docker Compose
- Bash (Linux/macOS) ou WSL (Windows)

### Teste 2 (Python)

- Python 3.8+
- pip
- venv (python3-venv)

---

## 📝 Notas Importantes

### SQL Server

- A senha do SA é `MyStrongPass123!`
- O container usa a porta `1433`
- Use a flag `-C` no sqlcmd para ignorar o certificado SSL
- O caminho do sqlcmd no SQL Server 2022 é `/opt/mssql-tools18/bin/sqlcmd`

### Python

- Sempre ative o venv antes de executar: `source venv/bin/activate`
- Para instalar novamente: `pip install -r requirements.txt`
- O venv está no `.gitignore` e não deve ser commitado

---

## 🔍 Resolução de Problemas

### Teste 1

**Problema:** `exec: "/opt/mssql-tools/bin/sqlcmd": no such file or directory`

- **Solução:** Use `/opt/mssql-tools18/bin/sqlcmd` ao invés de `/opt/mssql-tools/bin/sqlcmd`

**Problema:** Porta 1433 já em uso

- **Solução:**
  ```bash
  docker compose down
  sudo lsof -i :1433
  # Matar processo ou mudar porta no docker-compose.yml
  ```

**Problema:** SQL Server não inicializa

- **Solução:** Aguarde mais tempo (até 60 segundos) ou verifique logs:
  ```bash
  docker compose logs -f
  ```

### Teste 2

**Problema:** `externally-managed-environment`

- **Solução:** Use venv:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```

**Problema:** `ModuleNotFoundError: No module named 'pytest'`

- **Solução:** Instale as dependências:
  ```bash
  source venv/bin/activate
  pip install -r requirements.txt
  ```

---

## 📚 Documentação Adicional

- [SQL Server Window Functions](https://learn.microsoft.com/en-us/sql/t-sql/queries/select-over-clause-transact-sql)
- [Python Binary Trees](https://docs.python.org/3/tutorial/datastructures.html)
- [Pytest Documentation](https://docs.pytest.org/)

---

## 👨‍💻 Autor

Desenvolvido como parte de um teste técnico.

**Data:** Janeiro 2026
