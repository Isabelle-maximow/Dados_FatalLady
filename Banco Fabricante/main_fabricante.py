import sqlite3

BANCO = "fatallady_fabricante.bd"
conexao = sqlite3.connect(BANCO)
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS FABRICANTE (
    ID_FABRICANTE INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Cidade TEXT NOT NULL,
    Estado TEXT NOT NULL,
    Pais TEXT NOT NULL
)
""")
conexao.commit()

sql = """INSERT INTO FABRICANTE (Nome, Cidade, Estado, Pais)
         VALUES (?, ?, ?, ?)"""

valores = [
    ("Fatal Lady", "São Paulo", "SP", "Brasil"),
    ("Moda Feminina", "Rio de Janeiro", "RJ", "Brasil"),
    ("Passarela Shoes", "Belo Horizonte", "MG", "Brasil"),
    ("Estilo & Conforto", "Curitiba", "PR", "Brasil"),
    ("Elegance Calçados", "Porto Alegre", "RS", "Brasil"),
    ("Trend Shoes", "Fortaleza", "CE", "Brasil"),
    ("Fashion Steps", "Salvador", "BA", "Brasil"),
    ("Urban Chic", "Florianópolis", "SC", "Brasil"),
    ("Classic Shoes", "Manaus", "AM", "Brasil"),
    ("Glamour Calçados", "Recife", "PE", "Brasil"),
]

cursor.executemany(sql, valores)
conexao.commit()

cursor.close()
conexao.close()
