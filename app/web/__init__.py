"""
  Created by lin at 2019-06-08
"""
from flask import Blueprint

web = Blueprint('web', __name__)

from app.web import book
