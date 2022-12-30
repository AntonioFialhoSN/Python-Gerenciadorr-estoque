from ProgamaRegistro.Interface import *
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve o erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')

def lerBanco(arq):
    try:
        a = open(arq)
    except:
        print('ERRO ao ler o arquivo!')
    else:
        Bancostr = a.readlines()
        Banco_de_DD = []
        for c in range(0, len(Bancostr)):
            index = Bancostr[c]
            if index[0] == '[':
                dic = {}
                indice = index[2:-2]
                d = indice.split()
                for x in range(0, len(d)):
                    if d[x] == "'Codigo':":
                        dic['Codigo'] = d[1][1:-2]
                    elif d[x] == "'Nome':":
                        Nome = []
                        fim = d.index("'Fabricante':")
                        for intervalo in range(3, fim):
                            Nome.append(d[intervalo])
                        nomestr = ''
                        for v in range(0, len(Nome)):
                            for x in range(0, len(Nome[v])):
                                letra = Nome[v][x]
                                if letra != "'" and letra != ",":
                                    nomestr += letra
                            nomestr += ' '
                        dic['Nome'] = nomestr.strip()
                    elif d[x] == "'Fabricante':":
                        Fabricante = []
                        fim = d.index("'Valor':")
                        ini = d.index("'Fabricante':")
                        for intervalo in range(ini + 1, fim):
                            Fabricante.append(d[intervalo])
                        nomestr = ''
                        for v in range(0, len(Fabricante)):
                            for x in range(0, len(Fabricante[v])):
                                letra = Fabricante[v][x]
                                if letra != "'" and letra != ",":
                                    nomestr += letra
                            nomestr += ' '
                        dic['Fabricante'] = nomestr.strip()
                    elif d[x] == "'Valor':":
                        dic['Valor'] = float(d[-1][0:-1])
                Banco_de_DD.append(dic.copy())
                dic.clear()
            elif index[-1] == ']':
                dic = {}
                indice = index[2:-2]
                d = indice.split()
                for x in range(0, len(d)):
                    if d[x] == "'Codigo':":
                        dic['Codigo'] = d[1][1:-2]
                    elif d[x] == "'Nome':":
                        Nome = []
                        fim = d.index("'Fabricante':")
                        for intervalo in range(3, fim):
                            Nome.append(d[intervalo])
                        nomestr = ''
                        for v in range(0, len(Nome)):
                            for x in range(0, len(Nome[v])):
                                letra = Nome[v][x]
                                if letra != "'" and letra != ",":
                                    nomestr += letra
                            nomestr += ' '
                        dic['Nome'] = nomestr.strip()
                    elif d[x] == "'Fabricante':":
                        Fabricante = []
                        fim = d.index("'Valor':")
                        ini = d.index("'Fabricante':")
                        for intervalo in range(ini + 1, fim):
                            Fabricante.append(d[intervalo])
                        nomestr = ''
                        for v in range(0, len(Fabricante)):
                            for x in range(0, len(Fabricante[v])):
                                letra = Fabricante[v][x]
                                if letra != "'" and letra != ",":
                                    nomestr += letra
                            nomestr += ' '
                        dic['Fabricante'] = nomestr.strip()
                    elif d[x] == "'Valor':":
                        dic['Valor'] = float(d[-1])
                Banco_de_DD.append(dic.copy())
                dic.clear()
            else:
                dic = {}
                indice = index[2:-2]
                d = indice.split()
                for x in range(0, len(d)):
                    if d[x] == "'Codigo':":
                        dic['Codigo'] = d[1][1:-2]
                    elif d[x] == "'Nome':":
                        Nome = []
                        fim = d.index("'Fabricante':")
                        for intervalo in range(3, fim):
                            Nome.append(d[intervalo])
                        nomestr = ''
                        for v in range(0, len(Nome)):
                            for x in range(0, len(Nome[v])):
                                letra = Nome[v][x]
                                if letra != "'" and letra != ",":
                                    nomestr += letra
                            nomestr += ' '
                        dic['Nome'] = nomestr.strip()
                    elif d[x] == "'Fabricante':":
                        Fabricante = []
                        fim = d.index("'Valor':")
                        ini = d.index("'Fabricante':")
                        for intervalo in range(ini + 1, fim):
                            Fabricante.append(d[intervalo])
                        nomestr = ''
                        for v in range(0, len(Fabricante)):
                            for x in range(0, len(Fabricante[v])):
                                letra = Fabricante[v][x]
                                if letra != "'" and letra != ",":
                                    nomestr += letra
                            nomestr += ' '
                        dic['Fabricante'] = nomestr.strip()
                    elif d[x] == "'Valor':":
                        dic['Valor'] = float(d[-1][0:-1])
                Banco_de_DD.append(dic.copy())
                dic.clear()
        return Banco_de_DD
    finally:
        a.close()

def SalvarBanco(nome,lista):
    try:
        a = open(nome,'wt+')
    except:
        print('Houve um ERRO na abertura do arquivo')
    else:
        for x in range(0, len(lista)):
            if x == 0:
                c = '[' + str(lista[x]) + ',\n'
            elif x == len(lista) - 1:
                c = ' ' + str(lista[x]) + ']\n'
            else:
                c = ' ' + str(lista[x]) + ',\n'
            a.write(c)
    finally:
        print('Salvo com sucesso!')



