import mysql.connector
import random

CONFIG_BANCO = {
    'host': 'localhost',
    'user': 'root',
    'password': 'dev1t@24',
    'database': 'fatallady',
}
conexao = mysql.connector.connect(**CONFIG_BANCO)
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS CLIENTES (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Senha VARCHAR(100) NOT NULL,
    CEP INT NOT NULL,
    Rua VARCHAR(100) NOT NULL,
    Cidade VARCHAR(50) NOT NULL,
    País VARCHAR(10) NOT NULL,
    Telefone BIGINT NOT NULL
)
""")
conexao.commit()

nomes = [
    "Ana", "Beatriz", "Carla", "Daniel", "Eduardo", "Fernanda", "Gabriel", "Helena",
    "Isabela", "João", "Kátia", "Lucas", "Mariana", "Natália", "Otávio", "Paula",
    "Ricardo", "Sofia", "Thiago", "Vinícius"
]
sobrenomes = [
    "Silva", "Souza", "Oliveira", "Santos", "Ferreira", "Rodrigues", "Almeida",
    "Costa", "Martins", "Araújo", "Lima", "Melo", "Barbosa", "Cunha", "Carvalho"
]
ruas = [
    "Rua das Flores", "Avenida Central", "Rua da Paz", "Travessa Bela Vista",
    "Rua São Jorge", "Rua do Comércio", "Avenida Brasil", "Rua das Palmeiras"
]
cidades = [
    "Boa Vista", "Itaqua", "Guararema", "Moema", "Itaim Bibi",
    "Itaquera", "São Caetano", "Osasco", "Sorocaba"
]

paises = ["Brasil", "Portugal"]

clientes = [
    ("Ana Silva", "ana@email.com", "senha123", 12345678, "Rua das Flores", "Moema", "Brasil", 11999999999),
    ("Carlos Souza", "carlos@email.com", "senha456", 87654321, "Av. Paulista", "Itaim Bibi", "Brasil", 11988888888),
    ("Maria Oliveira", "maria@email.com", "senha789", 11223344, "Rua Verde", "Guararema", "Brasil", 11977777777),
    ("João Santos", "joao@email.com", "senha321", 44332211, "Rua Azul", "Osasco", "Brasil", 11966666666),
    ("Beatriz Costa", "beatriz@email.com", "senha654", 55667788, "Av. Central", "Sorocaba", "Brasil", 11955555555)
]

for _ in range(1000):
    nome_completo = f"{random.choice(nomes)} {random.choice(sobrenomes)}"
    email = nome_completo.replace(" ", ".").lower() + str(random.randint(1,9999)) + "@email.com"
    senha = f"senha{random.randint(1000,9999)}"
    cep = random.randint(10000000, 99999999)
    rua = random.choice(ruas)
    cidade = random.choice(cidades)
    pais = random.choice(paises)
    telefone = random.randint(11940000000, 11949999999) 

    clientes.append((nome_completo, email, senha, cep, rua, cidade, pais, telefone))

sql = """
INSERT INTO CLIENTES (Nome, Email, Senha, CEP, Rua, Cidade, País, Telefone)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""
cursor.executemany(sql, clientes)
conexao.commit()

cursor.close()
conexao.close()

