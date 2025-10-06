import pymysql
import random

# CONFIG_BANCO = {
#     'host': 'localhost',
#     'user': 'isabelle',
#     'password': 'mimiebella',
#     'database': 'fatallady',
#     'charset': 'utf8mb4'
# }

import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

# Connect to the database
try:
    connection = psycopg2.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        dbname=DBNAME
    )
    print("Connection successful!")
    
    # Create a cursor to execute SQL queries
    cursor = connection.cursor()
    
    # Example query
    cursor.execute("SELECT NOW();")
    result = cursor.fetchone()
    print("Current Time:", result)

    # Close the cursor and connection
    cursor.close()
    connection.close()
    print("Connection closed.")

except Exception as e:
    print(f"Failed to connect: {e}")

# Conectar ao banco
import random

# Dados base
marca = "Fatal Lady"
cores = ["Preto", "Branco", "Nude", "Vermelho", "Marrom", "Bege", "Cinza", "Dourado", "Prata"]
categorias = ["Sandália", "Bota", "Salto Alto", "Rasteirinha", "Sapatilha"]
tamanhos = ["35/38", "37/40", "38/41", "39/42"]
quantidades = list(range(10, 61))

# Produtos iniciais
produtos_iniciais = [
    ("Scarpin Clássico Preto", 189.90, 25, "Fatal Lady", "36/39", "Salto Alto"),
    ("Sandália Salto Alto Nude", 159.99, 30, "Fatal Lady", "36/38", "Sandália"),
    ("Sapatilha Verniz Vermelha", 99.90, 40, "Fatal Lady", "35/39", "Sapatilha"),
    ("Bota Cano Curto Couro", 249.90, 15, "Fatal Lady", "37/40", "Bota"),
    ("Sandália Rasteira Dourada", 89.90, 60, "Fatal Lady", "35/40", "Rasteirinha"),
    ("Bota Over The Knee Preta", 329.90, 10, "Fatal Lady", "36/39", "Bota"),
    ("Sandália Gladiadora Preta", 129.90, 15, "Fatal Lady", "38/39", "Sandália"),
    ("Bota Coturno Feminina Marrom", 219.90, 20, "Fatal Lady", "37/40", "Bota"),
    ("Sapatilha Bico Fino Nude", 109.90, 35, "Fatal Lady", "37/38", "Sapatilha"),
    ("Sandália Meia Pata Vermelha", 189.90, 12, "Fatal Lady", "35/36", "Sandália"),
    ("Peep Toe Preto Verniz", 159.90, 18, "Fatal Lady", "37/38", "Salto Alto"),
    ("Bota Montaria Marrom", 289.90, 14, "Fatal Lady", "38/39", "Bota"),
    ("Sandália Salto Fino Prata", 199.90, 16, "Fatal Lady", "37/38", "Sandália")
]

# Gerar mais 1000 produtos aleatórios
produtos_aleatorios = []
for _ in range(1000):
    categoria = random.choice(categorias)
    cor = random.choice(cores)
    nome = f"{categoria} {cor}"
    preco = round(random.uniform(69.9, 329.9), 2)
    estoque = random.choice(quantidades)
    tamanho = random.choice(tamanhos)
    produtos_aleatorios.append((nome, preco, estoque, marca, tamanho, categoria))

# Juntar todos os produtos
todos_produtos = produtos_iniciais + produtos_aleatorios

# Gerar comandos SQL
with open("inserir_produtos.sql", "w", encoding="utf-8") as f:
    f.write("INSERT INTO PRODUTOS (Nome, Preco, Estoque, Marca, Tamanhos, Categoria) VALUES\n")
    for i, p in enumerate(todos_produtos):
        linha = f"('{p[0]}', {p[1]}, {p[2]}, '{p[3]}', '{p[4]}', '{p[5]}')"
        if i < len(todos_produtos) - 1:
            linha += ",\n"
        else:
            linha += ";\n"
        f.write(linha)