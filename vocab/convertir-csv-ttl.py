# conversion des termes de vocabulaire
import csv, re

vocabFile = 'vocab.csv'

# Initialisations
extractedData = []

# Chargement des données
with open(vocabFile, 'r+', newline = '') as csvFile:
    for row in csv.DictReader(csvFile, delimiter = ','):
        extractedData.append(dict(row))

# Écriture du fichier Turtle
with open('vocab.ttl', 'w') as ABox:
    for subject in extractedData:
        for i, (property, value) in enumerate(subject.items()):

            if value == '':
                continue

            if 1 < i < len(subject):
                assertions += ' ;\n'

            if property == 'URI':
                assertions = value + ' rdf:type owl:NamedIndividual ,\n'
            elif property == 'rdf:type':
                assertions += '\t\t' + subject['rdf:type']
            else:
                assertions += '\t' + property + ' ' + value

        assertions += ' .\n\n'
        ABox.write(assertions)
