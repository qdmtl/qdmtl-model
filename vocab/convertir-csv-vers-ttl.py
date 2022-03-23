import csv, re

# Paramètres
# tcID = '001' # Test case ID
blankNodes = [] # Blank nodes (index du champ)
#folder = 'tc-' + tcID
vocabFile = 'vocab.qdmtl.ca.csv'

# Initialisations
extractedData = []
propWithBlankNodeValue = {}
propWithBlankNode = []

# Chargement des données
with open(vocabFile, 'r+', newline = '') as csvFile:
    for row in csv.DictReader(csvFile, delimiter = ','):
        extractedData.append(dict(row))

# Identification des propriétés avec noeuds vides
for i, key in enumerate(extractedData[0].keys()):
    if i in blankNodes:
        propWithBlankNode.append(key)

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
            elif property in propWithBlankNode :
                propWithBlankNodeValue[property] = value
            else:
                assertions += '\t' + property + ' ' + value

        if propWithBlankNodeValue:

            assertions += ' ;\n\trico:hasOrHadIdentifier '

            for i, (property, value) in enumerate(propWithBlankNodeValue.items()):
                assertions += '[\n'
                assertions += '\t\trdf:type rico:Identifier ;\n'
                assertions += '\t\trico:hasIdentifierType ' + property + ' ;\n'
                assertions += '\t\trico:textualValue ' + value + ' .\n\t]'

                if i < len(propWithBlankNodeValue) - 1:
                    assertions += ' , '

            else:
                propWithBlankNodeValue = {}

        assertions += ' .\n\n'
        ABox.write(assertions)
