import pymysql
import random

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

# Dados de exemplo para comentários
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

# Simular avaliações aleatórias
for _ in range(100):  # ajuste o número conforme necessidade
    id_cliente = random.randint(1, 50)    # IDs fictícios de clientes
    id_produto = random.randint(1, 1000)  # IDs fictícios de produtos
    comentario = random.choice(comentarios_exemplo)
    avaliacoes.append((id_cliente, id_produto, comentario))

# Inserir dados na tabela
sql_avaliacoes = """
INSERT INTO AVALIACOES (ID_CLIENTE, ID_PRODUTO, Comentario)
VALUES (%s, %s, %s)
"""
cursor.executemany(sql_avaliacoes, avaliacoes)
conexao.commit()

print(f"{len(avaliacoes)} avaliações inseridas com sucesso!")

# Fechar conexão
cursor.close()
conexao.close()
