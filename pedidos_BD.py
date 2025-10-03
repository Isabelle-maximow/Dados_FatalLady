import pymysql
import random
import datetime

CONFIG_BANCO = {
    'host': 'localhost',
    'user': 'isabelle',
    'password': 'mimiebella',
    'database': 'fatallady',
    'charset': 'utf8mb4'
}

# Conectar ao banco
conexao = pymysql.connect(**CONFIG_BANCO)
cursor = conexao.cursor()


# Criar tabela PEDIDOS
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

# Buscar IDs válidos de clientes
cursor.execute("SELECT ID FROM CLIENTES")
ids_clientes = [row[0] for row in cursor.fetchall()]

# Se não houver clientes cadastrados, evita erro
if not ids_clientes:
    print("⚠ Nenhum cliente encontrado! Insira clientes antes de gerar pedidos.")
else:
    status_opcoes = ["Pendente", "Pago", "Enviado", "Concluído", "Cancelado"]
    pedidos = []

    # Gerar 1000 pedidos
    for _ in range(1000):  
        id_cliente = random.choice(ids_clientes)
        data = datetime.date(
            random.randint(2020, 2025),   # ano
            random.randint(1, 12),        # mês
            random.randint(1, 28)         # dia
        )
        status = random.choice(status_opcoes)
        valor_total = round(random.uniform(50.0, 2000.0), 2)

        pedidos.append((id_cliente, data, status, valor_total))

    # Inserir no banco
    sql = """
    INSERT INTO PEDIDOS (ID_CLIENTE, Data, Status, ValorTotal)
    VALUES (%s, %s, %s, %s)
    """
    cursor.executemany(sql, pedidos)
    conexao.commit()

    print(f"{len(pedidos)} pedidos inseridos com sucesso!")

# Encerrar conexão
cursor.close()
conexao.close()
