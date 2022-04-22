## DB model
- For simplicity and demo purposes, article table is purposedly flattened. I.e authors identities are inside tables instead of separate author table connected via relations to article and comment table

## HTTP request
- request to the testApi are synchronous as there is no gain using async request just for one request. Contrary there would be some penalty to init other threads

## Postgres
- uses implicit role admin&postgres

## Flask
- Uses development server Werkzeug, PROD version should support NGINX and Gunicorn 

## Improvements
- add some unit tests
