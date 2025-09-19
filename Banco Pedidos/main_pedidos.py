import sqlite3

BANCO = "fatallady_pedidos.bd" 
conexao = sqlite3.connect(BANCO)
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS PEDIDOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_CLIENTE INTEGER NOT NULL,
    Data TEXT NOT NULL,
    Status TEXT NOT NULL,
    ValorTotal REAL NOT NULL,
    FOREIGN KEY (ID_CLIENTE) REFERENCES CLIENTES(ID)
);
""")
conexao.commit()

sql = """INSERT INTO PEDIDOS (ID_CLIENTE, Data, Status, ValorTotal)
         VALUES (?, ?, ?, ?)"""

valores = [
    (1, "2025-09-10", "Pago", 459.70),
    (2, "2025-09-11", "Enviado", 249.90),
    (3, "2025-09-11", "Entregue", 189.90),
    (4, "2025-09-12", "Pendente", 329.90),
    (5, "2025-09-12", "Pago", 159.99),
    (6, "2025-09-13", "Enviado", 299.90),
    (7, "2025-09-13", "Entregue", 209.90),
    (8, "2025-09-14", "Pago", 499.80),
    (9, "2025-09-14", "Pendente", 139.90),
    (10, "2025-09-15", "Pago", 289.90),
    (11, "2025-09-15", "Pago", 179.90),
    (12, "2025-09-15", "Enviado", 229.90),
    (13, "2025-09-16", "Entregue", 329.90),
    (14, "2025-09-16", "Pendente", 149.90),
    (15, "2025-09-17", "Pago", 189.90),
    (16, "2025-09-17", "Pago", 269.90),
    (17, "2025-09-17", "Enviado", 319.90),
    (18, "2025-09-18", "Entregue", 379.90),
    (19, "2025-09-18", "Pago", 199.90),
    (20, "2025-09-18", "Pendente", 89.90),
    (1, "2025-09-19", "Pago", 259.90),
    (2, "2025-09-19", "Enviado", 349.90),
    (3, "2025-09-20", "Pago", 129.90),
    (4, "2025-09-20", "Entregue", 219.90),
    (5, "2025-09-20", "Pago", 399.90),
    (6, "2025-09-21", "Pago", 189.90),
    (7, "2025-09-21", "Enviado", 279.90),
    (8, "2025-09-21", "Entregue", 499.90),
    (9, "2025-09-22", "Pendente", 149.90),
    (10, "2025-09-22", "Pago", 339.90),
    (11, "2025-09-22", "Pago", 219.90),
]

cursor.executemany(sql, valores)
conexao.commit()

cursor.close()
conexao.close()
