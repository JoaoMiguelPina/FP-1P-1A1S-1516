# Pedro Caldeira 83539, Joao Pina 85080, grupo 20 

def soma_tuplos(t1,t2):        #funcao auxiliar para somar tuplos com o mesmo tamanho 
    calculo = [0] * len(t1)
    for i in range(len(t1)):
        for i in range(len(t2)):
            calculo[i] = t1[i] + t2[i]
    return tuple(calculo)


def mandatos(nr_mandatos, nr_votos):
    mandatos_atribuidos = 0
    lista = list(nr_votos)          #de forma a tornar o processo mais simples transformamos o tuplo que e imutavel numa lista
    lista_mandatos = []
    
    while len(lista_mandatos)!=len(nr_votos):
        lista_mandatos = lista_mandatos+[0, ]
    
    while mandatos_atribuidos < nr_mandatos:     #metodo de d'hondt
        indice = 0
        for i in range(len(lista)):
            if lista[i] > lista[indice]:
                indice = i
            elif indice != i and lista[indice] == lista[i]:    #se houver um empate
                if nr_votos[indice] > nr_votos[i]:
                    indice = i       
            
        lista_mandatos[indice] = lista_mandatos[indice] + 1
        
        lista[indice] = nr_votos[indice] / (lista_mandatos[indice] + 1)
        
        mandatos_atribuidos = mandatos_atribuidos + 1       
    return tuple(lista_mandatos)

def assembleia(votacoes):
    resultado=(0,)*15
    deputados=(16, 3, 19, 3, 4, 9, 3, 9, 4, 10, 47, 2, 39, 9, 18, 6, 5, 9, 5, 6, 2, 2)
    i = 0
    while i<22:
        mandatos_auxiliar = mandatos(deputados[i], votacoes[i])     #mandatos auxiliar e um tuplo intermedio
        resultado = soma_tuplos(resultado, mandatos_auxiliar)       
        i = i + 1
    return resultado      

def max_mandatos(votacoes):               #por fim definimos a ultima funcao onde sabemos qual o partido vencedor
    deputados = assembleia(votacoes)
    vencedor = 0
    sinal_empate = False
    for i in range(len(deputados)):
        if deputados[i] > deputados[vencedor]:
            vencedor = i
            sinal_empate = False
        elif i != vencedor and deputados[i] == deputados[vencedor]:
            sinal_empate = True            
        
    partidos = ('PDR\tPartido Democratico Republicano',\
                'PCP-PEV\tCDU-Coligacao Democratica Unitaria',\
                'PPD/PSD-CDS/PP\tPortugal a Frente',\
                'MPT\tPartido da Terra',\
                'L/TDA\tLIVRE/Tempo de Avancar',\
                'PAN\tPessoas-Animais-Natureza',\
                'PTP-MAS\tAgir',\
                'JPP\tJuntos Pelo Povo',\
                'PNR\tPartido Nacional Renovador',\
                'PPM\tPartido Popular Monarquico',\
                'NC\tNos, Cidadaos!',\
                'PCTP/MRPP\tPartido Comunista dos Trabalhadores Portugueses',\
                'PS\tPartido Socialista',\
                'B.E.\tBloco de Esquerda',\
                'PURP\tPartido Unido dos Reformados e Pensionistas')
    if sinal_empate:
        return 'Empate tecnico'
    else:
        return partidos[vencedor]
                
    