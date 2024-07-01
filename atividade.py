def cadastrar(dicio):
    dicio[input("digite o login que deseja cadastrar: ")] = input("digite a senha que deseja cadastrar: ")

def addestoque(x):
    nome = input("digite o nome do produto: ")
    pq = [int(input("digite o preço do produto:")),int(input("digite a quantidade deste produto: "))]
    x [nome] = pq
def atuestoque(y):
    while True:
        nome = input("digite o nome do produto que deseja atualizar: ")
        if nome not in y:
            print("este produto nao esta no estoque")
        else:
            y[nome] = [int(input("digite o preço do produto:")),int(input("digite a quantidade deste produto: "))]
            break
def catalogo(z):
    for i in z:
        print(f"{i}: preço:{z[i][0]}R$,quantidade:{z[i][1]}")

def addcarinho(x, y):
    while True:
        nome= input("digite o nome do produto que deseja comprar: ")
        quantidade = int(input("digite quantos produtos deseja pegar: "))
        if nome not in x:
            print("produto invalido")
        elif quantidade> x[nome][1]:
            print("quantidade de produtos eh maior que a loja tem a oferecer")
        else:
            #fazer quantidade
            
            y.append({f"{nome}":[x[nome][0],quantidade]})
            break
def remover(x):
    removee = input("digite o nome do produto que deseja remover: ")
    for i in range(len(x)):
        if x[i] == removee:
            x.pop[i]

def visualizar(x):
    print("produtos que estao no seu carrinho: ")
    for i in x:
        for y,z in i.items():
            print(f"produto:{y}, preço:{z[0]} e quantidade:{z[1]}")

def comprar(produtos, carrinho):
    total = 0
    f = {}
    for i in carrinho:
        for x,y in i.items():
            total= total + (y[0]*y[1])
            f[x] = y[0]*y[1]
    print(f"o valor total da sua compra foi: {total}")
    t = int(input("digite 1 para realizar a compra, e 2 para retornar ao menu: "))
    if t == 1:
        print("compra realizada!!")
        for j in carrinho:
            for x,y in j.items():
                produtos[x] = [y[0], produtos[x][1] - y[1]]
        global historico
        historico.append(f)
    elif t ==2:
        return
def hist(x):
    contador = 0
    for i in x:
        contador+=1
        print(f"na compra {contador}: ")
        for p,z in i.items():
            print(f"foi comprado o produto: {p}, gastando um total de {z}R$")

historico = []
carrinho =[]
produtos={}
senhas = {'adm':'adm123'}


def login(senhas):
    while True:
        Login = input("digite seu login: ")
        senha = input("digite sua senha: ")
        if Login in senhas.keys() and senha in senhas.values(): 
            print("senha valida!")
            if Login=='adm':
                global adm
                adm=True
            break
        else:
            print("senha invalida, digite novamente!")
login(senhas)
while True:
    
    print("-"*60)
    print("digite qual dessas operações deseja realizar:")
    print("-"*60)
    print("1 - CADASTRAR USUARIO")
    print("2 - CATALOGO DE PRODUTOS")
    print("3 - ADICIONAR PRODUTO NO CARRINHO")
    print("4 - REMOVER PRODUTO DO CARRINHO")
    print("5 - VISUALIZAR CARRINHO")
    print("6 - TERMINAR COMPRA")
    print("7 - HISTORICO DE COMPRA")
    print("8 - ADMINISTRAR ESTOQUE")
    print("9 - SAIR")
    print("10 - fazer login novamente")
    print("-"*60)
    tarefa = int(input("digite a operaçao que deseja realizar: "))
    if tarefa ==1:
        if adm ==False:
            print("apenas ADM pode realizar essa função")
        else:
            print("-"*60)
            cadastrar(senhas)
            print(senhas)
            print("-"*60)
    if tarefa ==8:
        if adm == False:
            print("-"*60)
            print("apenas ADM pode realizar essa função")
            print("-"*60)
        else:
            print("-"*60)
            variavel = int(input("digite 1 para atualizar estoque, 2 para adicionar adcionar estoque: "))
            if variavel ==2:
                addestoque(produtos)
                print(produtos)
                print("-"*60)
            if variavel ==1:
                atuestoque(produtos)
                print(produtos)
                print("-"*60)
    if tarefa == 2:
        print("-"*60)
        catalogo(produtos)
        print("-"*60)
    if tarefa ==3:
        print("-"*60)
        addcarinho(produtos, carrinho)
        print(carrinho)
        print("-"*60)
    if tarefa ==4:
        print("-"*60)
        remover(carrinho)
        print(carrinho)
        print("-"*60)
    if tarefa ==5:
        print("-"*60)
        visualizar(carrinho)
        print("-"*60)
    if tarefa ==6:
        print("-"*60)
        comprar(produtos,carrinho)
        print(historico)
        print("-"*60)
    if tarefa == 7:
        print("-"*60)
        hist(historico)
        print("-"*60)      
    if tarefa == 9:
        break
    if tarefa == 10:
        adm = False
        print("-"*60)
        login(senhas)
        print("-"*60)