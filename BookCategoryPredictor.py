# mongoimport --db dbName --collection collectionName --file fileName.json
# import a json collection in mongodb
import Models

Models.getBooks()

# step1 - Acquisire in un dataframe tutti i dati del DB
# step2 - Rimuovere i campi non utili
# step3 - Fill dei campi vuoti con il valore medio e fill delle descrizioni con il titolo
# step4 - matrice termini-doc con le long description
# step5 - unione della matrice con le altre feature
# step6 - addestramento modelli predittivi