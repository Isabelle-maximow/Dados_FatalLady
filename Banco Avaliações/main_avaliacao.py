import sqlite3

BANCO = "fatallady_avaliacao.bd"
conexao = sqlite3.connect(BANCO)
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS AVALIACAO (
    ID_AVALIACAO INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_CLIENTE INTEGER NOT NULL,
    ID_PRODUTO INTEGER NOT NULL,
    Comentario TEXT NOT NULL,
    FOREIGN KEY (ID_CLIENTE) REFERENCES CLIENTES(ID),
    FOREIGN KEY (ID_PRODUTO) REFERENCES PRODUTOS(ID)
)
""")
conexao.commit()

sql = """INSERT INTO AVALIACAO (ID_CLIENTE, ID_PRODUTO, Comentario)
         VALUES (?, ?, ?)"""

valores = [
    (1, 1, "Excelente scarpin, muito confortável!"),
    (2, 3, "Sandália linda, mas o salto é um pouco alto para mim."),
    (3, 5, "Sapatilha perfeita para o dia a dia."),
    (4, 7, "Bota de ótima qualidade, couro macio."),
    (5, 2, "Sandália bonita, chegou rápido."),
    (6, 4, "Tênis confortável e moderno."),
    (7, 6, "Adorei a anabela, super estilosa."),
    (8, 8, "Bota over the knee linda, mas apertada no cano."),
    (9, 9, "Mule confortável e elegante."),
    (10, 10, "Oxford perfeito para trabalhar, muito confortável."),
    (1, 11, "Sandália gladiadora bonita, mas um pouco dura no início."),
    (2, 12, "Tamanco ótimo, recomendo."),
    (3, 13, "Bota coturno muito resistente."),
    (4, 14, "Sapatilha nude linda, entrega rápida."),
    (5, 15, "Chinelo básico, bom para casa."),
    (6, 16, "Sandália meia pata linda, adorei a cor."),
    (7, 17, "Peep toe elegante, super confortável."),
    (8, 18, "Tênis slip on confortável e leve."),
    (9, 19, "Bota montaria perfeita para o inverno."),
    (10, 20, "Sandália salto fino maravilhosa!"),
]

cursor.executemany(sql, valores)
conexao.commit()

cursor.close()
conexao.close()
