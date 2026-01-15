#!/bin/bash

echo "🚀 Parando containers anteriores..."
docker compose down

echo "🚀 Iniciando SQL Server..."
docker compose up -d

echo "⏳ Aguardando SQL Server inicializar..."
sleep 35

echo "📊 Executando script de inicialização do banco de dados..."
docker exec -it sqlserver_teste /opt/mssql-tools18/bin/sqlcmd \
    -S localhost -U SA -P 'MyStrongPass123!' -C \
    -i /init.sql

echo "✅ Banco de dados configurado!"
echo ""
echo "🎯 Executando a query da solução..."
docker exec -it sqlserver_teste /opt/mssql-tools18/bin/sqlcmd \
    -S localhost -U SA -P 'MyStrongPass123!' -C \
    -i /task1.sql
echo ""
echo "📝 Para conectar manualmente use:"
echo "docker exec -it sqlserver_teste /opt/mssql-tools18/bin/sqlcmd -S localhost -U SA -P 'MyStrongPass123!' -C"
echo ""
echo "Ou conecte via cliente externo:"
echo "Server: localhost,1433"
echo "User: SA"
echo "Password: MyStrongPass123!"
echo "Database: TesteDB"