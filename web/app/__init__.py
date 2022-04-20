from flask import Flask
from app.config import Config
from flask_bootstrap import Bootstrap
import asyncio

app = Flask(__name__)

app.config.from_object(Config)

from app.blueprints.page import page

app.register_blueprint(page)
bootstrap = Bootstrap(app)
from app.db.services import init_db

asyncio.run(init_db())
