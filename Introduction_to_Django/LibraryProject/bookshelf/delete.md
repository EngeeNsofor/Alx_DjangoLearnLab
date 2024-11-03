# Delete Operation

## Input

```python
# Delete the book instance
book.delete()

# Verify deletion by checking for any books in the database
Book.objects.all()
```

## Output
```python
(1, {'bookshelf.Book': 1})
<QuerySet []>
```