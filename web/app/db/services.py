from tortoise import Tortoise
import app.db.models
from datetime import datetime


from app import app


def constring() -> str:
    """
    Based on settings value returns constring for psg DB
    """

    _postgres_host = app.config.get("POSTGRES_HOST")
    _postgres_port = app.config.get("POSTGRES_PORT")
    _postgres_user = app.config.get("POSTGRES_USER")
    _postgres_password = app.config.get("POSTGRES_PASSWORD")
    _postgres_db = app.config.get("POSTGRES_DB")

    return f"postgres://{_postgres_user}:{_postgres_password}@{_postgres_host}:{_postgres_port}/{_postgres_db}"


async def init_db():
    await Tortoise.init(db_url=constring(), modules={"models": ["app.db.models"]})
    await Tortoise.generate_schemas()
    await Tortoise.close_connections()


def str_to_datetime(date_str: str) -> datetime:
    """_summary_ convert date time sr representation from API do dateime object"""
    return datetime.strptime(date_str, "%d.%m.%Y %H:%M:%S")
