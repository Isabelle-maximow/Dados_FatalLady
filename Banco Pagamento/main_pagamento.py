import sqlite3

BANCO = "fatallady_pagamentos.bd"
conexao = sqlite3.connect(BANCO)
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS PAGAMENTOS (
    ID_PAGAMENTO INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_PEDIDO INTEGER NOT NULL,
    ID_CLIENTE INTEGER NOT NULL,
    MetodoPagamento TEXT NOT NULL,
    DataPagamento TEXT NOT NULL,
    FOREIGN KEY (ID_PEDIDO) REFERENCES PEDIDOS(ID),
    FOREIGN KEY (ID_CLIENTE) REFERENCES CLIENTES(ID)
)
""")
conexao.commit()

sql = """INSERT INTO PAGAMENTOS (ID_PEDIDO, ID_CLIENTE, MetodoPagamento, DataPagamento)
         VALUES (?, ?, ?, ?)"""


valores = [
    (1, 1, "Cartão de Crédito", "2025-09-18"),
    (2, 3, "Pix", "2025-09-18"),
    (3, 5, "Boleto", "2025-09-19"),
    (4, 2, "Cartão de Débito", "2025-09-19"),
    (5, 4, "Pix", "2025-09-20"),
    (6, 6, "Cartão de Crédito", "2025-09-20"),
    (7, 2, "Pix", "2025-09-20"),
    (8, 7, "Boleto", "2025-09-21"),
    (9, 8, "Cartão de Crédito", "2025-09-21"),
    (10, 1, "Pix", "2025-09-21"),
    (11, 9, "Cartão de Débito", "2025-09-22"),
    (12, 10, "Cartão de Crédito", "2025-09-22"),
    (13, 11, "Pix", "2025-09-22"),
    (14, 12, "Boleto", "2025-09-23"),
    (15, 13, "Cartão de Crédito", "2025-09-23"),
    (16, 14, "Pix", "2025-09-23"),
    (17, 15, "Cartão de Débito", "2025-09-24"),
    (18, 16, "Cartão de Crédito", "2025-09-24"),
    (19, 17, "Pix", "2025-09-24"),
    (20, 18, "Boleto", "2025-09-25"),
    (21, 19, "Pix", "2025-09-25"),
    (22, 20, "Cartão de Crédito", "2025-09-25"),
    (5, 4, "Cartão de Crédito", "2025-09-26"), # cliente com mais de 1 pagamento
    (7, 2, "Boleto", "2025-09-26"),
    (10, 1, "Cartão de Crédito", "2025-09-27"),
]

cursor.executemany(sql, valores)
conexao.commit()

cursor.close()
conexao.close()
