book = {
    'title': 'My first book',
    'author': 'Renan',
    'year':1996
}
print(book)
print(book['year'])

MyTitle=book['title']
MyTitle=book.get('title')

print(MyTitle)

print(book.keys())
print(book.values())

book['pages']=254
print(book)
#book['year']=1984
book.update({'year':1997})
print(book)
if 1997 in book:#you can look for keys but not values
    print('Yes it is in the dictonary')

book.pop('year')
print(book)
book.popitem()
print(book)

#del book(deletes the whole dictionary
#print(book)

#book.clear()(clear the whole dictionary)
#print(book)

students={
    'vid111':{
        'name':'George',
         'gpa':2.0
    },
    'vid222':{
    'name':'Samantha',
    'gpa':2.5
    },
    'vid333':{
        'name':'Jenny',
        'gpa':3.0
    }}
print(students['vid111']['name'],students['vid111']['gpa'])
print(students['vid222']['name'],students['vid222']['gpa'])
print(students['vid333']['name'],students['vid333']['gpa'])