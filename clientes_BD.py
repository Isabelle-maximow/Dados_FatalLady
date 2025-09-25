import mysql.connector
import random

CONFIG_BANCO = {
    'host': 'localhost',
    'user': 'root',
    'password': 'dev1t@24',
    'database': 'fatallady_bd',
}
conexao = mysql.connector.connect(**CONFIG_BANCO)
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS CLIENTES (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Senha VARCHAR(100) NOT NULL,
    CEP INT NOT NULL,
    Rua VARCHAR(100) NOT NULL,
    Cidade VARCHAR(50) NOT NULL,
    País VARCHAR(10) NOT NULL,
    Tell. INT NOT NULL
)
""")
conexao.commit()

cidades_ficticias = [
    "Boa vista", "Itaqua", "Guararema", "Moema", "Itaim Bibi",
    "Itaquera", "", "São Caetano", "Osasco", "Sorocaba"
]

# valores = [
#     ("Marilyn Monroe", 189.90, 25, random.choice(marcas_ficticias), "36/39", "Sapatos Femininos"),
#     ("Elizabeth Taylor", 159.99, 30, random.choice(marcas_ficticias), "36/38", "Sapatos Femininos"),
#     ("Scarlett Johansson", 99.90, 40, random.choice(marcas_ficticias), "35/39", "Sapatos Femininos"),
#     ("Jennifer Lawrence", 249.90, 15, random.choice(marcas_ficticias), "37/40", "Sapatos Femininos"),
#     ("Tênis Casual Branco", 179.90, 50, random.choice(marcas_ficticias), "36/39", "Sapatos Femininos"),
#     ("Anabela Espadrille Bege", 139.90, 20, random.choice(marcas_ficticias), "37/38", "Sapatos Femininos"),
#     ("Sandália Rasteira Dourada", 89.90, 60, random.choice(marcas_ficticias), "35/40", "Sapatos Femininos"),
#     ("Bota Over The Knee Preta", 329.90, 10, random.choice(marcas_ficticias), "36/39", "Sapatos Femininos"),
#     ("Mule Salto Bloco Caramelo", 149.90, 18, random.choice(marcas_ficticias), "35/39", "Sapatos Femininos"),
#     ("Oxford Feminino Verniz Preto", 169.90, 22, random.choice(marcas_ficticias), "36/39", "Sapatos Femininos"),
#     ("Sandália Gladiadora Preta", 129.90, 15, random.choice(marcas_ficticias), "38/39", "Sapatos Femininos"),
#     ("Tamanco Plataforma Preto", 119.90, 25, random.choice(marcas_ficticias), "37/39", "Sapatos Femininos"),
#     ("Bota Coturno Feminina Marrom", 219.90, 20, random.choice(marcas_ficticias), "37/40", "Sapatos Femininos"),
#     ("Sapatilha Bico Fino Nude", 109.90, 35, random.choice(marcas_ficticias), "37/38", "Sapatos Femininos"),
#     ("Chinelo Slide Preto", 69.90, 50, random.choice(marcas_ficticias), "38/39", "Sapatos Femininos"),
#     ("Sandália Meia Pata Vermelha", 189.90, 12, random.choice(marcas_ficticias), "35/36", "Sapatos Femininos"),
#     ("Peep Toe Preto Verniz", 159.90, 18, random.choice(marcas_ficticias), "37/38", "Sapatos Femininos"),
#     ("Tênis Slip On Bege", 139.90, 28, random.choice(marcas_ficticias), "37/38", "Sapatos Femininos"),
#     ("Bota Montaria Marrom", 289.90, 14, random.choice(marcas_ficticias), "38/39", "Sapatos Femininos"),
#     ("Sandália Salto Fino Prata", 199.90, 16, random.choice(marcas_ficticias), "37/38", "Sapatos Femininos"),
# ]

modelos = [
    "Camila Passos", "Violet Ferreira", "Rhiannon Pires", "Maria Eduarda", "Safira Tophollo", "Anabela Rick", "Raphaella Morgan", "Mavi Ravioli",
    "Rosangela Rosa", "Catherine Earnshaw", "Nelly Marcondes", "Margott Robbie", "Nicole Kidman", "Coturno", "Montaria", "Gladiadora"
]
cores = ["Preto", "Branco", "Nude", "Vermelho", "Marrom", "Bege", "Cinza", "Dourado", "Prata", "Caramelo"]
categorias = ["Sapatos Femininos", "Sapatos Masculinos", "Infantis", "Calçados Esportivos"]
tamanho = ["35/38", "37/40", " 38/41", "38/41", "39/42"]
quantidades = list(range(10, 61))

for _ in range(1000):
    modelo = random.choice(modelos)
    cor = random.choice(cores)
    nome = f"{modelo} {cor}"
    preco = round(random.uniform(69.9, 329.9), 2)
    quantidade = random.choice(quantidades)
    marca = random.choice(marcas_ficticias)
    tamanhos = random.choice(tamanho)
    categoria = random.choice(categorias)
    valores.append((nome, preco, quantidade, marca, tamanhos, categoria))

sql = """
INSERT INTO PRODUTOS (Nome, Preco, Estoque, Marca, Tamanhos, Categoria)
VALUES (%s, %s, %s, %s, %s, %s)
"""

cursor.executemany(sql, valores)
conexao.commit()
cursor.close()
conexao.close()
