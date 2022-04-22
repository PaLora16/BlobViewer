## Solution

This is an example of Flask, Tortoise ORM and Marshmallow validation. App requests TestApi for a blog fiction articles.
There is a Flask and CLI part. Use pure MVC design pattern,

### BL logic Flask

- Flask part fetchs articles from TestApi all the time.

### BL logic CLI

1. Check if article id is saved in DB table -> retrieve article & print on stdout -> end.
2. Try to fetch article from TestApi.
3. If article id not returned from TestApi -> error messages -> end.
4. Save article to DB
5. Print formatted article on stdout.

### Running Flask solution
- working directory: web 
- run : python main.py .

### Running CLI solution
- working directory: web 
- run : python cli.py ***article_id***

