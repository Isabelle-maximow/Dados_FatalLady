import sqlite3

BANCO = "fatallady_bd.bd"
conexao = sqlite3.connect(BANCO)
cursor = conexao.cursor()

cursor.execute(""" 
CREATE TABLE IF NOT EXISTS PRODUTOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Preco REAL NOT NULL,
    Estoque INTEGER NOT NULL,
    Marca TEXT NOT NULL,
    Tamanho TEXT NOT NULL,
    Categoria TEXT NOT NULL
)""")
conexao.commit()

# produtos
sql = """INSERT INTO PRODUTOS (Nome, Preco, Estoque, Marca, Tamanho, Categoria)
         VALUES (?, ?, ?, ?, ?, ?)"""

valores = [
    ("Scarpin Clássico Preto", 189.90, 25, "Fatal Lady", "34 a 39", "Scarpin"),
    ("Scarpin Verniz Vermelho", 209.90, 18, "Fatal Lady", "34 a 40", "Scarpin"),
    ("Sandália Salto Alto Nude", 159.99, 30, "Fatal Lady", "35 a 40", "Sandália"),
    ("Sandália Salto Bloco Bege", 149.90, 20, "Fatal Lady", "34 a 39", "Sandália"),
    ("Sapatilha Verniz Vermelha", 99.90, 40, "Fatal Lady", "33 a 39", "Sapatilha"),
    ("Sapatilha Estampada Floral", 89.90, 35, "Fatal Lady", "34 a 39", "Sapatilha"),
    ("Bota Cano Curto Couro Preto", 249.90, 15, "Fatal Lady", "34 a 39", "Bota"),
    ("Bota Cano Longo Camurça Marrom", 299.90, 12, "Fatal Lady", "35 a 40", "Bota"),
    ("Tênis Casual Branco", 179.90, 50, "Fatal Lady", "34 a 40", "Tênis"),
    ("Tênis Chunky Rosa", 199.90, 22, "Fatal Lady", "34 a 39", "Tênis"),
    ("Anabela Espadrille Bege", 139.90, 20, "Fatal Lady", "34 a 39", "Anabela"),
    ("Anabela Floral Azul", 159.90, 16, "Fatal Lady", "34 a 39", "Anabela"),
    ("Sandália Rasteira Dourada", 89.90, 60, "Fatal Lady", "33 a 39", "Sandália"),
    ("Sandália Rasteira Prata", 79.90, 55, "Fatal Lady", "33 a 38", "Sandália"),
    ("Bota Over The Knee Preta", 329.90, 10, "Fatal Lady", "35 a 40", "Bota"),
    ("Mule Salto Bloco Caramelo", 149.90, 18, "Fatal Lady", "34 a 39", "Mule"),
    ("Mule Bordado Bege", 139.90, 14, "Fatal Lady", "34 a 38", "Mule"),
    ("Oxford Feminino Verniz Preto", 169.90, 22, "Fatal Lady", "34 a 39", "Oxford"),
    ("Oxford Nude Fosco", 159.90, 19, "Fatal Lady", "34 a 39", "Oxford"),
    ("Sandália Gladiadora Preta", 129.90, 15, "Fatal Lady", "35 a 40", "Sandália"),
    ("Tamanco Plataforma Preto", 119.90, 25, "Fatal Lady", "34 a 39", "Tamanco"),
    ("Tamanco Metalizado Dourado", 129.90, 20, "Fatal Lady", "34 a 39", "Tamanco"),
    ("Bota Coturno Feminina Marrom", 219.90, 20, "Fatal Lady", "34 a 39", "Bota"),
    ("Bota Coturno Verniz Preto", 229.90, 18, "Fatal Lady", "34 a 40", "Bota"),
    ("Sapatilha Bico Fino Nude", 109.90, 35, "Fatal Lady", "33 a 38", "Sapatilha"),
    ("Sapatilha Preta Básica", 89.90, 42, "Fatal Lady", "34 a 39", "Sapatilha"),
    ("Chinelo Slide Preto", 69.90, 50, "Fatal Lady", "34 a 39", "Chinelo"),
    ("Chinelo Slide Rosa", 74.90, 45, "Fatal Lady", "34 a 38", "Chinelo"),
    ("Sandália Meia Pata Vermelha", 189.90, 12, "Fatal Lady", "34 a 39", "Sandália"),
    ("Sandália Meia Pata Preta", 199.90, 15, "Fatal Lady", "35 a 40", "Sandália"),
    ("Peep Toe Preto Verniz", 159.90, 18, "Fatal Lady", "34 a 39", "Peep Toe"),
    ("Peep Toe Bege Fosco", 169.90, 20, "Fatal Lady", "34 a 39", "Peep Toe"),
    ("Tênis Slip On Bege", 139.90, 28, "Fatal Lady", "34 a 39", "Tênis"),
    ("Tênis Slip On Preto", 149.90, 25, "Fatal Lady", "34 a 39", "Tênis"),
    ("Bota Montaria Marrom", 289.90, 14, "Fatal Lady", "35 a 40", "Bota"),
    ("Bota Montaria Preta", 299.90, 12, "Fatal Lady", "35 a 40", "Bota"),
    ("Sandália Salto Fino Prata", 199.90, 16, "Fatal Lady", "34 a 39", "Sandália"),
    ("Sandália Salto Fino Ouro", 209.90, 14, "Fatal Lady", "34 a 39", "Sandália"),
    ("Mocassim Feminino Marrom", 129.90, 30, "Fatal Lady", "34 a 39", "Mocassim"),
    ("Mocassim Verniz Preto", 139.90, 28, "Fatal Lady", "34 a 39", "Mocassim"),
]

# inserir todos
cursor.executemany(sql, valores) # executemany serve para inserir varios valores
conexao.commit()

# Encerrar conexão
cursor.close()
conexao.close()
