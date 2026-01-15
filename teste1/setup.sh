#!/bin/bash

echo "🚀 Iniciando SQL Server..."
docker-compose up -d

echo "⏳ Aguardando SQL Server inicializar (30 segundos)..."
sleep 30

echo "📊 Executando script de inicialização do banco de dados..."
docker exec -it sqlserver_teste /opt/mssql-tools/bin/sqlcmd \
    -S localhost -U SA -P 'MyStrongPass123!' \
    -i /docker-entrypoint-initdb.d/init.sql

echo "✅ Banco de dados configurado!"
echo ""
echo "Para executar a query da solução:"
echo "docker exec -it sqlserver_teste /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P 'MyStrongPass123!' -i /teste1/task1.sql"
echo ""
echo "Ou conecte usando:"
echo "Server: localhost,1433"
echo "User: SA"
echo "Password: MyStrongPass123!"
echo "Database: TesteDB"
