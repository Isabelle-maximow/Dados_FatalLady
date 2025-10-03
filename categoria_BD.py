import pymysql

CONFIG_BANCO = {
    'host': 'localhost',
    'user': 'isabelle',
    'password': 'mimiebella',
    'database': 'fatallady',
    'charset': 'utf8mb4'
}

# Conexão com o banco
conexao = pymysql.connect(**CONFIG_BANCO)
cursor = conexao.cursor()

# Criação da tabela CATEGORIA
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
    ("Sapatilha", "Modelo fechado, sem salto, muito usado no cotidiano por seu conforto.")
]

# Inserção dos dados
sql = """
INSERT INTO CATEGORIA (Nome, Descricao)
VALUES (%s, %s)
"""
cursor.executemany(sql, categorias)
conexao.commit()

print(f"{len(categorias)} categorias inseridas com sucesso!")

# Encerrar a conexão
cursor.close()
conexao.close()
