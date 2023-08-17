Mongo DB notes

Following [tutorial](https://www.youtube.com/watch?v=c2M-rlkkT5o&t=335s) to learn Mongo db.

# Commands
- `show dbs`
- `use *database name*` this command will use or create a database
- `db.createCollection(*collection name*)` this method will create a collection
- `db.*collection name*.insertOne({*fieldname*: *value*, *fieldname*:*value*})` insert a document
- `db.*collection name*.insertMany({...}, {...}, {...})` field pairs do not need to be consistent

## looking for documents in students collection
- `db.students.find()` to display the documents
- `db.students.find().sort({name:1})` using a document, 1 for alphabetical and -1 for reverse alphabetical
- `db.students.find().limit(3)` limit returned results


### Datatypes
- string
- int
- double (float or decimal)
- boolean
- date `new Date('2023-01-02T00:00)` no argument means current UTC
- null
- array `['biology', 'chemistry', 'physics']`
- nested document `{street: '123 fake street', city: 'london', postcode: 'w2'}` (an object)





