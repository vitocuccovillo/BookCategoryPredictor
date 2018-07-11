# mongoimport --db dbName --collection collectionName --file fileName.json
# import a json collection in mongodb
import Models
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# step1 - Acquisire in un dataframe tutti i dati del DB
# step2 - Rimuovere i campi non utili
# step3 - Fill dei campi vuoti con il valore medio e fill delle descrizioni con il titolo
# step4 - matrice termini-doc con le long description
# step5 - unione della matrice con le altre feature
# step6 - addestramento modelli predittivi

books = Models.GetAllBooks()
books_df = pd.DataFrame(books)
books_df.set_index('bid')

drop_columns = ['thumbnailUrl', 'isbn', '_id','authors']
books_df.drop(drop_columns, inplace=True, axis=1)

books_df['longDescription'].fillna(books_df['title'], inplace=True)
books_df['pageCount'].fillna(books_df['pageCount'].median, inplace=True)
books_df['categories'].fillna('none', inplace=True)
books_df['cat'] = books_df['categories'].map(lambda x: x[0] if len(x) > 0 else 'default')
books_df.drop('categories', inplace=True, axis=1)

vect = CountVectorizer(ngram_range=(1,2),stop_words='english')
matrix = vect.fit_transform(books_df['longDescription']) # restituisce la matrice termini-doc
freqs = [(word, matrix.getcol(idx).sum()) for word, idx in vect.vocabulary_.items()]
# sort from largest to smallest
for phrase, times in sorted(freqs, key=lambda x: -x[1])[:25]:
    print(phrase, times)

