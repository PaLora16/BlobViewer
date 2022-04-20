
class Config(object):

    ARTICLE_BY_ID_URL = "http://denver.sensearena.com/api/v1/article/"

    ARTICLES_URL = "http://denver.sensearena.com/api/v1/articles"

    # Running in Docker-compose config example
    # POSTGRES_HOST = "postgres"
    # POSTGRES_PORT = "5342"
    # POSTGRES_USER = "postgres"
    # POSTGRES_PASSWORD = "password"

    # Running in Python environment config examples
    POSTGRES_HOST = "localhost"
    POSTGRES_PORT = "5433"
    POSTGRES_USER = "postgres"
    POSTGRES_PASSWORD = "password"
    POSTGRES_DB = "postgres"
