import mysql.connector

# configurar a conexão com o banco de dados:
CONFIG_BANCO = {
    'host': 'localhost', # local do servidor de banco
    'user': 'root', # usuario que vi logar no servidor
    'password': 'fatalady', # senha definida no servidor 
    'database': 'fatallady_bd', # nome do banco de dados
}

conexao = mysql.connector.connect(**CONFIG_BANCO) # conectando
cursor = conexao.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS PRODUTOS (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Preco DECIMAL(10,2) NOT NULL,
    Estoque INT NOT NULL,
    Marca VARCHAR(50) NOT NULL,
    Tamanho VARCHAR(10) NOT NULL,
    Categoria VARCHAR(50) NOT NULL)""")
conexao.commit()

# inserindo os dados
sql = """INSERT INTO PRODUTOS (Nome, Preco, Estoque, Marca, Tamanho, Categoria)
         VALUES (%s, %s, %s, %s, %s, %s)"""

valores = [
    ("Scarpin Clássico Preto", 189.90, 25, "Fatal Lady", "38", "Sapatos Femininos"),
    ("Sandália Salto Alto Nude", 159.99, 30, "Fatal Lady", "37", "Sapatos Femininos"),
    ("Sapatilha Verniz Vermelha", 99.90, 40, "Fatal Lady", "36", "Sapatos Femininos"),
    ("Bota Cano Curto Couro", 249.90, 15, "Fatal Lady", "39", "Sapatos Femininos"),
    ("Tênis Casual Branco", 179.90, 50, "Fatal Lady", "38", "Sapatos Femininos"),
    ("Anabela Espadrille Bege", 139.90, 20, "Fatal Lady", "37", "Sapatos Femininos"),
    ("Sandália Rasteira Dourada", 89.90, 60, "Fatal Lady", "36", "Sapatos Femininos"),
    ("Bota Over The Knee Preta", 329.90, 10, "Fatal Lady", "39", "Sapatos Femininos"),
    ("Mule Salto Bloco Caramelo", 149.90, 18, "Fatal Lady", "38", "Sapatos Femininos"),
    ("Oxford Feminino Verniz Preto", 169.90, 22, "Fatal Lady", "37", "Sapatos Femininos"),
    ("Sandália Gladiadora Preta", 129.90, 15, "Fatal Lady", "38", "Sapatos Femininos"),
    ("Tamanco Plataforma Preto", 119.90, 25, "Fatal Lady", "39", "Sapatos Femininos"),
    ("Bota Coturno Feminina Marrom", 219.90, 20, "Fatal Lady", "38", "Sapatos Femininos"),
    ("Sapatilha Bico Fino Nude", 109.90, 35, "Fatal Lady", "37", "Sapatos Femininos"),
    ("Chinelo Slide Preto", 69.90, 50, "Fatal Lady", "38", "Sapatos Femininos"),
    ("Sandália Meia Pata Vermelha", 189.90, 12, "Fatal Lady", "36", "Sapatos Femininos"),
    ("Peep Toe Preto Verniz", 159.90, 18, "Fatal Lady", "39", "Sapatos Femininos"),
    ("Tênis Slip On Bege", 139.90, 28, "Fatal Lady", "37", "Sapatos Femininos"),
    ("Bota Montaria Marrom", 289.90, 14, "Fatal Lady", "38", "Sapatos Femininos"),
    ("Sandália Salto Fino Prata", 199.90, 16, "Fatal Lady", "37", "Sapatos Femininos"),
]

# inserir todos
cursor.executemany(sql, valores)
conexao.commit()

print(cursor.rowcount, "sapatos femininos foram inseridos!")

# Encerrar conexão
cursor.close()
conexao.close()