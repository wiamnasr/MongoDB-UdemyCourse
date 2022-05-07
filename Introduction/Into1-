### In order to connect to MongoDB, after successfull installation of MongoDB and the shell, run the below in the terminal widow:

```

mongosh


```

### By default some databases are shipped with MongoDB, to check out what databases are there:

```

show dbs


```


### Connecting to a database, below we are connecting to shop database, even if it did not exist this command will create a new database called shop

```

use shop


```


### Creating a new collection, like creating a database above, this can also be done on the fly

>   Below we are creating a new collection on the fly called products and using inserOne to insert one new product, passing a JSON object to it


>   In the JSON object we can add our keys and their respective values (key-value)

>   Notice how the double quotes can be ommitted here for the keys with MongoDB

```

db.products.insertOne({name: "A Book", price: 15.88})


```


### Having a look at our data, find() without any extra arguments, gives us the whole data in a collection

```

db.products.find()

# or

db.products.find().pretty()


```


>   An Example of an embedded document:

```

db.products.insertOne({name: "A Computer", price: 1229.99, description: "A high quality computer.", details: {cpu: "Intel i7 xxxxx", memory: 32}})


```