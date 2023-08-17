Mongo DB notes

Following [tutorial](https://www.youtube.com/watch?v=c2M-rlkkT5o&t=335s) to learn Mongo db.

# Commands
- `show dbs`
- `use *database name*` this command will use or create a database
- `db.createCollection(*collection name*)` this method will create a collection
- `db.*collection name*.insertOne({*fieldname*: *value*, *fieldname*:*value*})` insert a document
- `db.*collection name*.insertMany({...}, {...}, {...})` field pairs do not need to be consistent

- `show collections`
- `db.createCollection('teachers', {capped:true, size: 10000000, max: 100}, {autoIndexId: false})` collection with 10mb size and 100 document limit
- `db.teachers.drop()` to drop a collection

## looking for documents in students collection
- `db.students.find()` to display the documents
- `db.students.find().sort({name:1})` using a document, 1 for alphabetical and -1 for reverse alphabetical {name} is the field and 1 (or -1) for alphabetical (up or down)
- `db.students.find().limit(3)` limit returned results
- `db.students.find().sort({gpa:1}.limit(1))` sort by gpa, alphabetically and return 1 result
- `db.students.find({name: "Spongebob"})` find Spongebob
- `db.students.find({fullTime: false})` find students where the boolean value of full time is set to false
- `db.students.find({gpa:4, fullTime: True})` similar to a where clause where both conditions are true
- `db.students.find({query}, {projection})` like SQL {where} and {which columns you want to select}
In compass, {query} SQL's where {projection} SQL's selected columns
- `db.students.find({}, {_id: false, name: true})` return all the documents but just the name

## Update
- `db.students.updateOne({filter} {update})` selection critera and update parameters
- `db.students.updateOne({name:'Spongebob'}, {$set:{fullTime:true}})` update (or create) a field for Spongebob that says he is a fulltime student - update boolean to true
- `db.students.updateOne({_id:ObjectId("64ddf98711b060548a9da86c")}, {$set:{fullTime:false}})` use the object Id to locate the document for update
- `db.students.updateOne({_id:ObjectId("64ddf98711b060548a9da86c")}, {$unset:{fullTime:''}})` remove a field by setting it to be an empty string
- `db.students.updateMany({}, {$set:{fullTime: false}})` empty braces to select everyone, set their FT status to false
- `db.students.updateMany({fullTime:{$exists: false}}, {$set:{fullTime: true}})` locate anyone who doesn't have a fulltime field, create the field and set it to true (won't affect the students who had a fullt time field already set to false)

### Datatypes
- string
- int
- double (float or decimal)
- boolean
- date `new Date('2023-01-02T00:00)` no argument means current UTC
- null
- array `['biology', 'chemistry', 'physics']`
- nested document `{street: '123 fake street', city: 'london', postcode: 'w2'}` (an object)
- more can be seen by pressing the pencil in compass to edit a document and set a field

## Export and Delete
- `db.students.deleteOne({filter})` select the document to delete
- `db.students.deleteOne({name: 'Larry})` delete Larry 
- `db.students.deleteMany({fullTime:false})` delete anyone who is a part-time student
- `db.student.deleteMany({registerDate:{$exists:false}})` if the registration field does not exist delete the document

## Comparison Operators denoted by $
- $ne `db.students.find({name:{$ne:'Spongebob'}})` !=, all names that are not Spongebob
- $lt `db.students.find({age:{$lt:27}})` <, less than age 27 
- $lte `db.students.find({age:{$lte:27}})` <=, less than or equal to age 27
- $gte `db.students.find({age:{$gte:27}})` >=, greater than or equal to age 27
- between `db.students.find({gpa:{$gte:3, $lte:4}})`
- $in `db.students.find({name:{$in:['Spongebob', 'Patrick', 'Sandy']}})`
- $nin `db.students.find({name:{$nin:['Spongebob', 'Patrick', 'Sandy']}})` not in

## Logical Operators
- $and `db.students.find({$and: [{fullTime:true}, {age:{$gte:22}}]})` find fulltime and younger than 22
- $or `db.students.find({$or: [{fullTime:true}, {age:{$gte:22}}]})` find fulltime or younger than 22
- $nor `db.students.find({$nor: [{fullTime:true}, {age:{$gte:22}}]})` find neither fulltime nor younger than 22
- $not `db.students.find({age:{$not:{$gte:30}}})` also returns null fields, all students less than 30 even those with null age

## Queries
- `db.getCollection('sales').find({date: { $gte: new Date('2014-04-04'), $lt: new Date('2014-04-05') }}).count()`
- run an aggregation and open a cursor to the results.
Use '.toArray()' to exhaust the cursor to return the whole result set.
You can use '.hasNext()/.next()' to iterate through the cursor page by page.
`db.getCollection('sales').aggregate([{ $match: { date: { $gte: new Date('2014-01-01'), $lt: new Date('2015-01-01') } } },{ $group: { _id: '$item', totalSaleAmount: { $sum: { $multiply: [ '$price''$quantity' ] } } } }]);`
Find all of the sales that occurred in 2014 and group the total sales for each product.

## Indexes
to speed up searching without using a linear search to look at every file
- `db.students.createIndex({name: 1})`
- `db.students.find({name:'Larry'}).explain('executionStats')` will show me how many files were looked at to achieve the reult, after indexing, just 1 in my small dataset of 5
- `db.students.getIndexes()` to view the indexes
- `db.students.dropIndex('name_1')` to drop an index I created

# connection string
mongodb://localhost:27017/