import mysql.connector
import random

CONFIG_BANCO = {
    'host': 'localhost',
    'user': 'root',
    'password': 'dev1t@24',
    'database': 'fatallady',
}

# Conexão com o banco
conexao = mysql.connector.connect(**CONFIG_BANCO)
cursor = conexao.cursor()

# Criar tabela CLIENTES (sem acento em nomes de colunas!)
cursor.execute("""
CREATE TABLE IF NOT EXISTS FABRICANTES (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Cidade VARCHAR(50) NOT NULL,
    Pais VARCHAR(30) NOT NULL,
    Estado VARCHAR(20) NOT NULL
)
""")
conexao.commit()

# Dados base
nomes = ["TechNova", "LuxWear", "VitaModa", "UrbanEdge", "PrimeStyle", "Fatal Lady"]
estados = ["SP", "RJ", "MG", "RS", "PR", "SC", "BA", "PE", "CE", "GO"]
cidades = ["Campinas", "Ribeirão Preto", "Santos", "Jundiaí", "Piracicaba", "Taubaté", "Barueri", "Franca", "Bauru"]
paises = ["Brasil", "Portugal"]

# Lista de clientes
fabricante = [
    ("TechNova", "Campinas", "Brasil", "SP"),
    ("LuxWear", "Ribeirão Preto", "Brasil", "SP"),
    ("VitaModa", "Santos", "Brasil", "SP"),
    ("UrbanEdge", "Jundiaí", "Brasil", "SP"),
    ("PrimeStyle", "Piracicaba", "Brasil", "SP"),
    ("Fatal Lady", "São Paulo", "Brasil", "SP")
]

# Gerar mais 1000 clientes aleatórios
for _ in range(1000):
    nome = random.choice(nomes)
    estado = random.choice(estados)
    cidade = random.choice(cidades)
    pais = random.choice(paises)

    fabricante.append((nome, cidade, pais, estado))

# Inserir clientes no banco
sql = """
INSERT INTO FABRICANTES (Nome, Cidade, Pais, Estado)
VALUES (%s, %s, %s, %s)
"""
cursor.executemany(sql, fabricante)
conexao.commit()

# Fechar conexão
cursor.close()
conexao.close()
