#!/usr/bin/env python3

'''
1. convertir les termes de vocabulaire : CSV -> TTL
2. concaténer
'''

import csv, re, shutil

# config
vocabFile = 'vocab/vocab.csv'
vocabFileTTL = 'vocab/vocab.ttl'
TBox = 'qdmtl.ttl'

# Initialisations
extractedData = []

'''
1. convertir
'''

# Chargement des données
with open(vocabFile, 'r+', newline = '') as csvFile:
    for row in csv.DictReader(csvFile, delimiter = ','):
        extractedData.append(dict(row))

# Écriture du fichier Turtle
with open(vocabFileTTL, 'w') as ABox:
    for subject in extractedData:
        for i, (property, value) in enumerate(subject.items()):

            if value == '':
                continue

            if 1 < i < len(subject):
                assertions += ' ;\n'

            # voir structure switch Python 3.10
            if property == 'URI':
                assertions = value + ' rdf:type owl:NamedIndividual ,\n'
            elif property == 'rdf:type':
                assertions += '\t\t' + subject['rdf:type']
            else:
                assertions += '\t' + property + ' ' + value

        assertions += ' .\n\n'
        ABox.write(assertions)

'''
2. concaténer
'''

with open(TBox,'a') as file:
    with open(vocabFileTTL,'r') as input:
        shutil.copyfileobj(input, file)