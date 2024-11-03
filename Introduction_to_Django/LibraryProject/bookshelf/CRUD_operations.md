# CRUD Operations

## Create Operation

### Input
```python
from bookshelf.models import Book

# Creating a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
```

### Output
```python
<Book: Book object (1)>
```


## Retrieve Operation

### Input

```python
# Retrieve the book by title
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
```

### Output
```python
('1984', 'George Orwell', 1949)
```


## Update Operation

### Input
```python
# Update the title of the book
book.title = "Nineteen Eighty-Four"
book.save()
book.title
```

### Output
```python
'Nineteen Eighty-Four'
```


## Delete Operation

### Input

```python
# Delete the book instance
book.delete()

# Verify deletion by checking for any books in the database
Book.objects.all()
```

### Output
```python
(1, {'bookshelf.Book': 1})
<QuerySet []>
```