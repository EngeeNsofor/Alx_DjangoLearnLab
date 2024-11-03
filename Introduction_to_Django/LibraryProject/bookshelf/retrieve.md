# Retrieve Operation


## Input

```python
# Retrieve the book by title
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
```

## Output
```python
('1984', 'George Orwell', 1949)
```

