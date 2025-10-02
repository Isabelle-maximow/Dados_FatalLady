import mysql.connector

CONFIG_BANCO = {
    'host': 'localhost',
    'user': 'root',
    'password': 'mimiebella',
    'database': 'fatallady',
}

# Conexão com o banco
conexao = mysql.connector.connect(**CONFIG_BANCO)
cursor = conexao.cursor()

# Criação da tabela CATEGORIAS
cursor.execute("""
CREATE TABLE IF NOT EXISTS CATEGORIA (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Descricao VARCHAR(500) NOT NULL
)
""")
conexao.commit()

# Dados de exemplo para categorias
categorias = [
    ("Sandália", "Calçados leves e abertos, ideais para dias quentes e combinações casuais ou sofisticadas."),
    ("Botas", "Calçados fechados, perfeitos para o inverno, com design que varia entre o clássico e o moderno."),
    ("Salto Alto", "Calçados elegantes com elevação no calcanhar, ideais para ocasiões formais e looks sofisticados."),
    ("Rasteirinha", "Modelos baixos e confortáveis, perfeitos para o dia a dia com um toque de estilo."),
    ("Sapatilha", "Modelo fechado, sem salto, muito usado no cotidiano por seu conforto."),
]

# Inserção dos dados
sql = """
INSERT INTO CATEGORIAS (Nome, Descricao)
VALUES (%s, %s)
"""

cursor.executemany(sql, categorias)
conexao.commit()

# Encerrar a conexão
cursor.close()
conexao.close()
