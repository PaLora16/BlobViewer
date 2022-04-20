## Solution

This example of Flask, Tortoise ORM, and Marshmallow validation for simple validation RestApi returning data for a blog fiction articles.
There is a Flask and CLI part.

### BL logic Flask

- Flask solution fetchs articles from TestApi all the time

### BL logic CLI

1. Check if article id is save in DB table -> fetch on
2. Try to fetch article from TestApi
3. Article not found -> error messages -> end
4. return article for next presentation

### Running Flask solution

- Python main.py from web folder

### Running CLI solution

* Python cli.py article_id
 from web folder
