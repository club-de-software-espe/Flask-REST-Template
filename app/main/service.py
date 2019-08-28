from flask import Blueprint
from app.constants import GET, POST, PUT
from .plugins import db
import json

urls = Blueprint('urls', __name__)

#define your routes here