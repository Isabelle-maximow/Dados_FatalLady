import mysql.connector
import random
import datetime

CONFIG_BANCO = {
    'host': 'localhost',
    'user': 'root',
    'password': 'dev1t@24',
    'database': 'fatallady_bd',
}
conexao = mysql.connector.connect(**CONFIG_BANCO)
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS PEDIDOS (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    ID_CLIENTE INT NOT NULL,
    Data DATE NOT NULL,
    Status VARCHAR(20) NOT NULL,
    ValorTotal DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (ID_CLIENTE) REFERENCES CLIENTES(ID)
)
""")
conexao.commit()

cursor.execute("SELECT ID FROM CLIENTES")
ids_clientes = [row[0] for row in cursor.fetchall()]

if not ids_clientes:
    print("Nenhum cliente encontrado. Insira clientes antes de gerar pedidos.")
else:
    status_opcoes = ["Pendente", "Pago", "Enviado", "Concluído", "Cancelado"]
    pedidos = []

for _ in range(1000):  
    id_cliente = random.choice(ids_clientes)
    data = datetime.date(
        random.randint(2020, 2025),   # ano
        random.randint(1, 12),        # mês
        random.randint(1, 28)         # dia (até 28 p/ evitar datas inválidas)
    )
    status = random.choice(status_opcoes)
    valor_total = round(random.uniform(50.0, 2000.0), 2)

    pedidos.append((id_cliente, data, status, valor_total))


sql = """
INSERT INTO PEDIDOS (ID_CLIENTE, Data, Status, ValorTotal)
VALUES (%s, %s, %s, %s)
"""
cursor.executemany(sql, pedidos)
conexao.commit()
print(f"{len(pedidos)} pedidos inseridos com sucesso!")
cursor.close()
conexao.close()
