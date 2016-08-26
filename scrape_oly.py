# -*- coding: utf-8
import re
import csv

dicio = {}

#Verifica participantes
def verifica_participante(s):
    """
    """
    return "Participants" in s

def verifica_header(s):
    """
    """
    match = re.search("(^\d{4}) .+, .* ", s)
    return match is not None

#deu match?
def is_match(match):
    return match is not None

#fazer cabecalho
def do_header(s):
    lista = []
    #ano
    match = re.search("(\d{4}) (.+), (.*)", s)
    lista.append(match.group(1))

    #cidade
    match = re.search("(\d{4}) (.+), (.*)", s)
    lista.append(match.group(2))

    #país
    match = re.search("(\d{4}) (.+), (.*)", s)
    lista.append(match.group(3))

    return lista

#fazer corpo
def do_body(s):
    lista = []
    #NOC participantes
    match = re.search("Participants: (\d+) .*, (\d+) events, (\d+,\d+|\d+) \wthletes(...|..)(\d,\d+|\d+) men, (\d,\d+|\d+) women", s)
    lista.append(match.group(1))

    #Eventos
    match = re.search("Participants: (\d+) .*, (\d+) events, (\d+,\d+|\d+) \wthletes(...|..)(\d,\d+|\d+) men, (\d,\d+|\d+) women", s)
    lista.append(match.group(2))

    #atletas
    match = re.search("Participants: (\d+) .*, (\d+) events, (\d+,\d+|\d+) \wthletes(...|..)(\d,\d+|\d+) men, (\d,\d+|\d+) women", s)
    lista.append(match.group(3))

    #homens
    match = re.search("Participants: (\d+) .*, (\d+) events, (\d+,\d+|\d+) \wthletes(...|..)(\d,\d+|\d+) men, (\d,\d+|\d+) women", s)
    lista.append(match.group(5))

    #Mulheres
    match = re.search("Participants: (\d+) .*, (\d+) events, (\d+,\d+|\d+) \wthletes(...|..)(\d,\d+|\d+) men, (\d,\d+|\d+) women", s)
    lista.append(match.group(6))

    return lista

header_is_written = False

with open('oly.txt', 'r') as arquivo:
    for row in arquivo:
        if verifica_header(row):
            dicio['ano'] = do_header(row)[0]
            dicio['cidade'] = do_header(row)[1]
            dicio['pais'] = do_header(row)[2]
            print do_header(row)[0]
            print do_header(row)[1]
            print do_header(row)[2]
        if verifica_participante(row):
            s1 = row
            s2 = next(arquivo)
            print s1[:-1]+s2
            print do_body(s1[:-1]+s2)
            dicio['nocs'] = do_body(s1[:-1]+s2)[0]
            dicio['eventos'] = do_body(s1[:-1]+s2)[1]
            dicio['atletas'] = do_body(s1[:-1]+s2)[2]
            dicio['homens'] = do_body(s1[:-1]+s2)[3]
            dicio['mulheres'] = do_body(s1[:-1]+s2)[4]
            with open('table.csv', 'ab') as f:
                w = csv.DictWriter(f, dicio.keys())
                if header_is_written is False:
                    w.writeheader()
                    header_is_written = True
                    print dicio
                w.writerow(dicio)

print dicio
