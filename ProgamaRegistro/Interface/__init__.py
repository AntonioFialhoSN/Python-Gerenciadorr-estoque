from ProgamaRegistro.BancoDD import *

# 1 =  Ao executar o sistema deve mostrar um menu para o usuário digitar quais operação deseja
# realizar
# 2 = Cadastrar ITEM
# 3 =  Alterar ITEM
# 4 = Excluir ITEM fornecendo o Código
# 5 = Localizar um ITEM pelo Código
# 6 = Listagem geral dos ITEMS (apresentando a quantidade geral, e o somatório / media dos valores numéricos).
# o critério 6 está no sistema principal

def entradaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válidc.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

def linha(tam = 52):
    return '=' * tam

def Titulo(txt):
    print(linha())
    print(txt.center(52))
    print(linha())
# a função menu, é a responsavel pelo critério 1 do projeto
def menu(lista):
    Titulo('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c:6} - {item}')
        c += 1
    print(linha())
    opc = entradaint('Sua opção: ')
    return opc

def showtabela(lista):
    print(linha(100))
    print(f'{"Codigo":^25}{"Nome":^25}{"Fabricante":^25}{"Valor":^25}')
    print(linha(100))
    for x in range(0, len(lista)):
        print(
            f'{lista[x]["Codigo"]:^25}{lista[x]["Nome"]:^25}{lista[x]["Fabricante"]:^25}{lista[x]["Valor"]:^25}')
    print(linha(100))
# todas as funções acima estão ligadas com a organização das informações e as entradas do programa.
# As funções em diante estão ligadas as funções desempenhadas pelo algoritmo, de acordo com o projeto.


def cadastro(Valor_QTD,Banco_Dados):
    Dados = {}
    for z in range(0, Valor_QTD):
        Dados['Codigo'] = str(input("Digite o código do produto: ")).strip().upper()
        Dados['Nome'] = str(input("Digite o nome do produto: ")).strip().upper()
        Dados['Fabricante'] = str(input("Digite o nome do Fabricante: ")).strip().upper()
        Dados['Valor'] = float(input("Digite o valor em reais ($): "))
        Banco_Dados.append(Dados.copy())
        Dados.clear()
    return Banco_Dados
# a função cadastro, é a responsavel pelo critério 2 do projeto

def ver_codigo(valor2, Banco_Dados):
    num = 0
    for x in range(0, len(Banco_Dados)):
        Cdg = Banco_Dados[x]['Codigo']
        if Cdg == valor2:
            print(f'intem: {Banco_Dados[x]}')
            num += 1
    if num == 0:
        print('Código não encontrado')

# a função ver_codigo, é a responsavel pelo critério 5 do projeto, mas fui além e criei para nome,
# fabricante e preço. Diferente do codigo, essas chaves retornam uma listas pois não são exclusivas
#  de um dado

def ver_nome(valor2, Banco_Dados):
    lista_encontrados = []
    for x in range(0, len(Banco_Dados)):
        Cdg = Banco_Dados[x]['Nome']
        if Cdg == valor2:
            lista_encontrados.append(Banco_Dados[x])
    if len(lista_encontrados) > 0:
        print(f'Encotrado/s {len(lista_encontrados)} intem/ns')
        showtabela(lista_encontrados)
    else:
        print('Material não encontrado')
    lista_encontrados.clear()

def ver_fabricante(valor2, Banco_Dados):
    lista_encontrados = []
    for x in range(0, len(Banco_Dados)):
        Cdg = Banco_Dados[x]['Fabricante']
        if Cdg == valor2:
            lista_encontrados.append(Banco_Dados[x])
    if len(lista_encontrados) > 0:
        print(f'Encotrado/s {len(lista_encontrados)} intem/ns')
        showtabela(lista_encontrados)
    else:
        print('Material não encontrado')
    lista_encontrados.clear()

def ver_preço(valor2, Banco_Dados):
    lista_encontrados = []
    for x in range(0, len(Banco_Dados)):
        Cdg = Banco_Dados[x]['Valor']
        if Cdg == valor2:
            lista_encontrados.append(Banco_Dados[x])
    if len(lista_encontrados) > 0:
        print(f'Encotrado/s {len(lista_encontrados)} intem/ns')
        showtabela(lista_encontrados)
    else:
        print('Material não encontrado')
    lista_encontrados.clear()

def altera_codigo(cdg, Banco_Dados):
    psç = 0
    for x in range(0, len(Banco_Dados)):
        if cdg == Banco_Dados[x]['Codigo']:
            psç = x + 1
            print(Banco_Dados[x])
    if psç > 0:
        Banco_Dados.remove(Banco_Dados[psç - 1])
        Dados = {}
        Dados['Codigo'] = str(input("Digite o código do equipamento: ")).strip().upper()
        Dados['Nome'] = str(input("Digite o nome do produto: ")).strip().upper()
        Dados['Fabricante'] = str(input("Digite o nome do Fabricante: ")).strip().upper()
        Dados['Valor'] = float(input("Digite o valor em reais ($): "))
        Banco_Dados.insert(psç - 1, Dados)
        print('=' * 52)
        print('Cadastrado com Sucesso'.center(52))
        print('=' * 52)
        return Banco_Dados
    else:
        print('=' * 52)
        print('Não foi encontrado')
        print('=' * 52)
# a função altera_codigo, é a responsavel pelo critério 3 do projeto

def del_codigo(cdg, Banco_Dados, seg_certeza):
    if seg_certeza == 'S':
        psç2 = 0
        for x in range(0, len(Banco_Dados)):
            if cdg == Banco_Dados[x]['Codigo']:
                psç2 = x
        Banco_Dados.remove(Banco_Dados[psç2])
        return Banco_Dados
    elif seg_certeza == 'N':
        print('voltando para o menu')
# a função del_codigo, é a responsavel pelo critério 4 do projeto

def media(x,y):
    media = x / y
    return round(media,1)

def registro_geral(Banco_Dados):
    qtd_pro = len(Banco_Dados)
    list_produto = []
    soma = 0
    for x in range(0, qtd_pro):
        soma += Banco_Dados[x]['Valor']
        if Banco_Dados[x]['Nome'] not in list_produto:
            list_produto.append(Banco_Dados[x]['Nome'])
    list_valor_num_pro = []
    for indice in range(0, len(list_produto)):
        soma_pro = 0
        num_pro = 0
        for x in range(0, qtd_pro):
            if Banco_Dados[x]['Nome'] == list_produto[indice]:
                soma_pro += Banco_Dados[x]['Valor']
                num_pro += 1
        list_valor_num_pro.append(soma_pro)
        list_valor_num_pro.append(num_pro)
    Titulo('Registro Geral')
    print(linha(75))
    print("Variável".center(50) + "Valor".center(25))
    print(linha(75))
    print('Quantidade geral de produtos(U)'.center(50) + f'{qtd_pro}'.center(25))
    print('Soma geral de todos os valores dos produtos ($)'.center(50) + f'{round(soma, 1)}'.center(25))
    print('Média geral de todos os valores dos produtos ($)'.center(50) + f'{media(soma, qtd_pro)}'.center(25))
    for x in range(0, len(list_produto)):
        print(f'Quantidade de {list_produto[x]} (U)'.center(50) + f'{list_valor_num_pro[x + x + 1]}'.center(25))
        print(f'Soma dos valores {list_produto[x]} ($)'.center(50) + f'{round(list_valor_num_pro[x + x])}'.center(25))
        print(f'Média dos valores {list_produto[x]} ($)'.center(
            50) + f'{media(list_valor_num_pro[x + x], list_valor_num_pro[x + x + 1])}'.center(25))
    print(linha(75))

def help_sistema():
    Titulo("Ajuda do sistema")
    Titulo("Cadastro")
    print('''O Cadastro é feito a partir dos atributos [Código; Nome;\n
Fabricante; Valor] basta escrever as caracteristica do produto. 
        ''')
    Titulo('Código')
    print('''Para gerar o código, siga o seguinte(1- As primeiras 3 letras do nome,\n
2- As primeiras 3 letras do fabricante, 3- As primeiras 2 letras ou número do \n
modelo, 4- e o número em do registro em razão de 10^4. Caso falte letras no \n
passo 1,2 e 3 complete com 1. (exemplo: Impressora, hp, modelo = i2, \n
1200 reais, sendo a vigésimo segundo do tipo no Banco. Código = IMPHP1I20022 \n
=> IMP ; HP1 ; I2 ; 0022). Caso tenha colocado um código repetido, basta ir\n
em alterar, que o último dado será alterado.
    ''' )
    Titulo("Outros atributos")
    print('Em relação aos outros atributos, a manipulação é \n mais tranquila pois não possui exclusividade')
