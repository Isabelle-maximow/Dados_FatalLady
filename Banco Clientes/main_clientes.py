import sqlite3

BANCO = "fatallady_clientes.bd"
conexao = sqlite3.connect(BANCO)
cursor = conexao.cursor()

# Criar tabela CLIENTES
cursor.execute(""" 
CREATE TABLE IF NOT EXISTS CLIENTES (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Email TEXT NOT NULL UNIQUE,
    Senha TEXT NOT NULL,
    Nome TEXT NOT NULL,
    CEP TEXT NOT NULL,
    Rua TEXT NOT NULL,
    Cidade TEXT NOT NULL,
    Pais TEXT NOT NULL,
    Telefone TEXT NOT NULL
)""")
conexao.commit()

sql = """INSERT INTO CLIENTES (Email, Senha, Nome, CEP, Rua, Cidade, Pais, Telefone)
         VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""

valores = [
    ("maria.silva@email.com", "senha123", "Maria Silva", "01001-000", "Rua das Flores, 123", "São Paulo", "Brasil", "(11) 99999-1234"),
    ("ana.oliveira@email.com", "abc456", "Ana Oliveira", "20040-010", "Av. Atlântica, 456", "Rio de Janeiro", "Brasil", "(21) 98888-5678"),
    ("juliana.santos@email.com", "pass789", "Juliana Santos", "30110-013", "Rua da Bahia, 789", "Belo Horizonte", "Brasil", "(31) 97777-9101"),
    ("carla.mendes@email.com", "fatal2025", "Carla Mendes", "40020-000", "Praça da Sé, 55", "Salvador", "Brasil", "(71) 96666-2020"),
    ("fernanda.costa@email.com", "123mudar", "Fernanda Costa", "80010-000", "Rua XV de Novembro, 321", "Curitiba", "Brasil", "(41) 95555-3030"),
    ("patricia.lima@email.com", "senha@2025", "Patrícia Lima", "69005-010", "Av. Eduardo Ribeiro, 987", "Manaus", "Brasil", "(92) 94444-5050"),
    ("beatriz.rocha@email.com", "minhasenha", "Beatriz Rocha", "88010-001", "Rua Felipe Schmidt, 77", "Florianópolis", "Brasil", "(48) 93333-6060"),
    ("aline.martins@email.com", "teste321", "Aline Martins", "60025-000", "Av. Beira Mar, 456", "Fortaleza", "Brasil", "(85) 92222-7070"),
    ("leticia.ferreira@email.com", "leticia#1", "Letícia Ferreira", "64000-100", "Rua das Acácias, 123", "Teresina", "Brasil", "(86) 91111-8080"),
    ("isabela.souza@email.com", "isa2025", "Isabela Souza", "49000-000", "Av. Beira Rio, 222", "Aracaju", "Brasil", "(79) 90000-9090"),
    ("giovanna.alves@email.com", "gio789", "Giovanna Alves", "79002-200", "Rua Dom Aquino, 345", "Campo Grande", "Brasil", "(67) 98888-1111"),
    ("rafaela.gomes@email.com", "rafa@2025", "Rafaela Gomes", "66010-000", "Av. Nazaré, 567", "Belém", "Brasil", "(91) 97777-2222"),
    ("camila.dias@email.com", "cami2025", "Camila Dias", "59020-000", "Rua das Hortênsias, 876", "Natal", "Brasil", "(84) 96666-3333"),
    ("tatiane.moreira@email.com", "tati321", "Tatiane Moreira", "77001-000", "Av. JK, 345", "Palmas", "Brasil", "(63) 95555-4444"),
    ("priscila.pereira@email.com", "pri123", "Priscila Pereira", "65010-000", "Rua Grande, 999", "São Luís", "Brasil", "(98) 94444-5555"),
    ("elisa.machado@email.com", "elisa456", "Elisa Machado", "68900-000", "Av. FAB, 234", "Macapá", "Brasil", "(96) 93333-6666"),
    ("sabrina.ramos@email.com", "sab@2025", "Sabrina Ramos", "69301-000", "Rua das Palmeiras, 12", "Boa Vista", "Brasil", "(95) 92222-7777"),
    ("victoria.cardoso@email.com", "vic999", "Victoria Cardoso", "69900-000", "Av. Getúlio Vargas, 77", "Rio Branco", "Brasil", "(68) 91111-8888"),
    ("luana.barbosa@email.com", "lua888", "Luana Barbosa", "76800-000", "Av. Sete de Setembro, 65", "Porto Velho", "Brasil", "(69) 90000-9999"),
    ("manuela.farias@email.com", "manu2025", "Manuela Farias", "45000-000", "Rua do Comércio, 321", "Vitória da Conquista", "Brasil", "(77) 98888-0000"),
]

# inserir todos
cursor.executemany(sql, valores)
conexao.commit()

cursor.close()
conexao.close()
