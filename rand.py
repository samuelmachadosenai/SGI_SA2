import random

def prod():


    a = {
    "nome": "Arroz Tipo 1",
    "preço": 14.90,
    "fornecedor": "CerealSul",
    "departamento": "Mercearia"
    }

    b = {
        "nome": "Biscoito Recheado",
        "preço": 3.50,
        "fornecedor": "DoceMania",
        "departamento": "Mercearia"
    }

    c = {
        "nome": "Café Torrado e Moído",
        "preço": 12.80,
        "fornecedor": "Café Brasil",
        "departamento": "Bebidas Quentes"
    }

    d = {
        "nome": "Detergente Neutro",
        "preço": 2.99,
        "fornecedor": "LimpaMais",
        "departamento": "Limpeza"
    }

    e = {
        "nome": "Enlatado de Ervilha",
        "preço": 4.20,
        "fornecedor": "ConservaMax",
        "departamento": "Mercearia"
    }

    f = {
        "nome": "Feijão Carioca",
        "preço": 8.90,
        "fornecedor": "GrãoFino",
        "departamento": "Mercearia"
    }

    g = {
        "nome": "Guaraná 2L",
        "preço": 7.50,
        "fornecedor": "Bebidas Tropicais",
        "departamento": "Bebidas"
    }

    h = {
        "nome": "Hortelã Fresca",
        "preço": 2.00,
        "fornecedor": "HortaNativa",
        "departamento": "Hortifruti"
    }

    i = {
        "nome": "Iogurte Natural",
        "preço": 5.60,
        "fornecedor": "Laticínios BelaVida",
        "departamento": "Laticínios"
    }

    j = {
        "nome": "Jiló",
        "preço": 3.10,
        "fornecedor": "Campo Verde",
        "departamento": "Hortifruti"
    }

    k = {
        "nome": "Ketchup Tradicional",
        "preço": 6.40,
        "fornecedor": "Molhos Brasil",
        "departamento": "Condimentos"
    }

    l = {
        "nome": "Leite Integral 1L",
        "preço": 4.90,
        "fornecedor": "Laticínios BoaFonte",
        "departamento": "Laticínios"
    }

    m = {
        "nome": "Macarrão Espaguete",
        "preço": 3.80,
        "fornecedor": "Massas Sol",
        "departamento": "Mercearia"
    }

    n = {
        "nome": "Nescau em Pó 400g",
        "preço": 9.90,
        "fornecedor": "CacauMix",
        "departamento": "Bebidas Quentes"
    }

    o = {
        "nome": "Óleo de Soja",
        "preço": 6.20,
        "fornecedor": "CozinhaPura",
        "departamento": "Mercearia"
    }

    p = {
        "nome": "Pão de Forma",
        "preço": 7.30,
        "fornecedor": "Panificadora Real",
        "departamento": "Padaria"
    }

    q = {
        "nome": "Queijo Mussarela Fatiado",
        "preço": 12.50,
        "fornecedor": "Laticínios BelaVida",
        "departamento": "Laticínios"
    }

    r = {
        "nome": "Refrigerante Cola 2L",
        "preço": 8.40,
        "fornecedor": "RefriStar",
        "departamento": "Bebidas"
    }

    s = {
        "nome": "Sabão em Pó 1kg",
        "preço": 14.30,
        "fornecedor": "CasaLimpa",
        "departamento": "Limpeza"
    }

    t = {
        "nome": "Tomate Italiano",
        "preço": 5.70,
        "fornecedor": "HortaNativa",
        "departamento": "Hortifruti"
    }

    u = {
        "nome": "Uva Crimson",
        "preço": 9.20,
        "fornecedor": "Frutas do Vale",
        "departamento": "Hortifruti"
    }

    v = {
        "nome": "Vinagre de Álcool",
        "preço": 3.00,
        "fornecedor": "SaborPuro",
        "departamento": "Condimentos"
    }

    w = {
        "nome": "Waffle Congelado",
        "preço": 11.90,
        "fornecedor": "FrozenGood",
        "departamento": "Congelados"
    }

    x = {
        "nome": "Xampu Neutro",
        "preço": 8.99,
        "fornecedor": "Beleza+",
        "departamento": "Higiene"
    }

    y = {
        "nome": "Yogurte de Morango",
        "preço": 5.70,
        "fornecedor": "Laticínios Frescor",
        "departamento": "Laticínios"
    }

    z = {
        "nome": "Zatar — Tempero",
        "preço": 4.50,
        "fornecedor": "Sabores do Oriente",
        "departamento": "Especiarias"
    }

    listA = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
    produto = random.choice(listA)

    nome = produto['nome']
    preco = produto['preço']


    return nome, preco