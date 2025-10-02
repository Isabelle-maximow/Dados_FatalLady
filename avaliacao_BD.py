import mysql.connector
import random

CONFIG_BANCO = {
    'host': 'localhost',
    'user': 'root',
    'password': 'mimiebella',
    'database': 'fatallady',
}

# Conectar ao banco de dados
conexao = mysql.connector.connect(**CONFIG_BANCO)
cursor = conexao.cursor()

# Criar tabela AVALIACOES
cursor.execute("""
CREATE TABLE IF NOT EXISTS AVALIACOES (
    ID_AVALIACAO INT AUTO_INCREMENT PRIMARY KEY,
    ID_CLIENTE INT NOT NULL,
    ID_PRODUTO INT NOT NULL,
    Comentario TEXT NOT NULL,
    FOREIGN KEY (ID_CLIENTE) REFERENCES CLIENTES(ID),
    FOREIGN KEY (ID_PRODUTO) REFERENCES PRODUTOS(ID)
)
""")
conexao.commit()

# Gerar dados fictícios para avaliações
comentarios_exemplo = [
    "Adorei o produto, chegou rápido!",
    "Tamanho ficou perfeito, recomendo.",
    "Cor linda, exatamente como na foto.",
    "Qualidade excelente, super confortável.",
    "Não gostei muito do acabamento.",
    "Produto veio com defeito, solicitei troca.",
    "Simplesmente amei! Vou comprar novamente.",
    "Entrega rápida e produto incrível!",
    "Muito bonito, mas o número ficou pequeno.",
    "Ótimo custo-benefício."
]

avaliacoes = []

# Simular avaliações aleatórias (ajuste conforme necessário)
for _ in range(100):  # Você pode mudar o número de avaliações aqui
    id_cliente = random.randint(1, 50)    # Simula clientes com ID de 1 a 50
    id_produto = random.randint(1, 1000)  # Supondo que você tem até 1000 produtos inseridos
    comentario = random.choice(comentarios_exemplo)
    avaliacoes.append((id_cliente, id_produto, comentario))

# Inserir dados na tabela AVALIACOES
sql_avaliacoes = """
INSERT INTO AVALIACOES (ID_CLIENTE, ID_PRODUTO, Comentario)
VALUES (%s, %s, %s)
"""

cursor.executemany(sql_avaliacoes, avaliacoes)
conexao.commit()

# Fechar conexões
cursor.close()
conexao.close()
