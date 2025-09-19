import sqlite3

BANCO = "fatallady_categoria.bd"
conexao = sqlite3.connect(BANCO)
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS CATEGORIA (
    ID_CATEGORIA INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Descricao TEXT NOT NULL
)
""")
conexao.commit()

sql = """INSERT INTO CATEGORIA (Nome, Descricao) VALUES (?, ?)"""

valores = [
    ("Salto", "Sapatos femininos de salto alto ou médio"),
    ("Bota", "Calçados femininos cobrindo o tornozelo ou cano alto"),
    ("Chinelo", "Calçados abertos, confortáveis e casuais"),
    ("Tênis", "Calçados esportivos ou casuais para o dia a dia"),
    ("Sapatilha", "Calçados baixos e fechados, confortáveis"),
    ("Mule", "Sapatos sem calcanhar, estilo casual e elegante"),
    ("Oxford", "Sapatos fechados com cadarço, elegantes"),
    ("Anabela", "Sandálias com salto anabela, confortável e moderno"),
    ("Peep Toe", "Sapatos com abertura nos dedos, femininos"),
    ("Tamanco", "Calçados com salto e plataforma, estilo casual"),
]

cursor.executemany(sql, valores)
conexao.commit()

cursor.close()
conexao.close()
