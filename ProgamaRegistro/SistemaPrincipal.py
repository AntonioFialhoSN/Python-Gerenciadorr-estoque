from ProgamaRegistro.Interface import *
from ProgamaRegistro.BancoDD import *
Titulo('MENU - BANCO DE DADOS DOS PRODUTOS V.1.0')
arq = 'BANCO_DADOS.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
Banco_Dados = lerBanco(arq)

while True:
    resposta = menu(['Cadastradas de produtos', 'Alterar informações do Banco de dados','localizar produto','Ver todos produtos cadastrados','Registro Geral','Help','Sair do sistema'])
    if resposta == 1:
        Valor_QTD = entradaint("DIGITE A QUANTIDADE DE REGISTROS:")
        cadastro(Valor_QTD,Banco_Dados)
        resp_de_safe = str(input("Deseja salvar?, digite ['S' - para sim / 'N' - para não]: "))[0].strip().upper()
        if resp_de_safe == 'S':
            SalvarBanco(arq, Banco_Dados)
    elif resposta == 2:
        while True:
            Titulo("Alterar informações do Banco de dados")
            n = menu(['Alterar dados', 'Excluir dados', 'Voltar ao menu'])
            if n == 1:
                cdg = str(input('Digite o Código: ')).strip().upper()
                altera_codigo(cdg,Banco_Dados)
            elif n == 2:
                cdg = str(input('Digite o Código para remover: ')).strip().upper()
                seg_certeza = str(input('Tem certeza que deseja remover [S:para sim/N:para não]:')).upper().strip()
                del_codigo(cdg,Banco_Dados,seg_certeza)
            elif n == 3:
                resp_de_safe = str(input("Deseja salvar?, digite ['S' - para sim/ 'N' - para não]: "))[0].strip().upper()
                if resp_de_safe == 'S':
                    SalvarBanco(arq, Banco_Dados)
                break
            else:
                print('Digite o números presente no menu :/ ')
    elif resposta == 3:
        while True:
            valor1 = menu(['buscar por Código','buscar por Nome','buscar por Fabricante','buscar por valor','Voltar ao menu'])
            if valor1 == 1:
                valor2 = str(input("Digite o Código: ")).upper().strip()
                ver_codigo(valor2,Banco_Dados)
            elif valor1 == 2:
                valor2 = str(input("Digite o Nome: ")).upper().strip()
                ver_nome(valor2, Banco_Dados)
            elif valor1 == 3:
                valor2 = str(input("Digite o Nome do Fabricante: ")).upper().strip()
                ver_fabricante(valor2, Banco_Dados)
            elif valor1 == 4:
                valor2 = float(input("Digite o Valor: "))
                ver_preço(valor2, Banco_Dados)
            elif valor1 == 5:
                break
            else:
                print('Digite uma das opções :/')
    elif resposta == 4:
        showtabela(Banco_Dados)
        # aqui esta uma parte do critério 6
    elif resposta == 5:
        registro_geral(Banco_Dados)
        # aqui esta outra parte do critério 6
    elif resposta == 6:
        help_sistema()
    elif resposta == 7:
        print("Salvando alterações no banco de dados")
        SalvarBanco(arq, Banco_Dados)
        print("Volte sempre!!!")
        break
    else:
        print('ERRO! Digite um número válido. :/')