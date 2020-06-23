from flask import Flask, _app_ctx_stack
from flask_cors import CORS
from sqlalchemy.orm import scoped_session
from config import Config
from . import models
from .db import SessionLocal,engine

models.Base.metadata.create_all(bind=engine)

app = Flask(__name__)
app.config.from_object( Config )
CORS(app)
app.session = scoped_session(SessionLocal, scopefunc=_app_ctx_stack.__ident_func__)
from app import routes
