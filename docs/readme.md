## Solution

This is an example of Flask, Tortoise ORM, and Marshmallow validation. App requests TestApi for a blog fiction articles.
There is a Flask and CLI part.

### BL logic Flask

- Flask part fetchs articles from TestApi all the time.

### BL logic CLI

1. Check if article id is saved in DB table -> retrieve article & presents on stdout
2. Otherwise try to fetch article from TestApi
3. If article id not returned from TestApi -> error messages -> end
4. Print formatted article on stdout

### Running Flask solution

- Python main.py from web folder

### Running CLI solution

- Python cli.py article_id
 from web folder
