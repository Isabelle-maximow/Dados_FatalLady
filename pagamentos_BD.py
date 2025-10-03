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

# Conexão com o banco
conexao = pymysql.connect(**CONFIG_BANCO)
cursor = conexao.cursor()

# Criar tabela PAGAMENTOS
cursor.execute("""
CREATE TABLE IF NOT EXISTS PAGAMENTOS (
    ID_PAGAMENTO INT AUTO_INCREMENT PRIMARY KEY,
    ID_PEDIDO INT NOT NULL,
    ID_CLIENTE INT NOT NULL,
    MetodoPagamento VARCHAR(30) NOT NULL,
    DataPagamento DATE NOT NULL,
    FOREIGN KEY (ID_PEDIDO) REFERENCES PEDIDOS(ID),
    FOREIGN KEY (ID_CLIENTE) REFERENCES CLIENTES(ID)
)
""")
conexao.commit()

# --- Buscar pedidos e seus clientes ---
cursor.execute("SELECT ID, ID_CLIENTE, Data FROM PEDIDOS")
pedidos = cursor.fetchall()  # [(id_pedido, id_cliente, data), ...]

if not pedidos:
    print("Nenhum pedido encontrado. Insira pedidos antes de gerar pagamentos.")
else:
    metodos = ["Cartão de Crédito", "Boleto", "Pix", "Transferência"]
    pagamentos = []

    for pedido in pedidos:
        id_pedido, id_cliente, data_pedido = pedido

        # converter para objeto datetime.date se vier como string
        if isinstance(data_pedido, str):
            data_pedido = datetime.datetime.strptime(data_pedido, "%Y-%m-%d").date()

        # gerar data de pagamento depois do pedido (0–10 dias depois)
        data_pagamento = data_pedido + datetime.timedelta(days=random.randint(0, 10))
        metodo = random.choice(metodos)

        pagamentos.append((id_pedido, id_cliente, metodo, data_pagamento))

    # Inserir pagamentos no banco
    sql = """
    INSERT INTO PAGAMENTOS (ID_PEDIDO, ID_CLIENTE, MetodoPagamento, DataPagamento)
    VALUES (%s, %s, %s, %s)
    """
    cursor.executemany(sql, pagamentos)
    conexao.commit()

    print(f"{len(pagamentos)} pagamentos inseridos com sucesso!")

# Fechar conexão
cursor.close()
conexao.close()
