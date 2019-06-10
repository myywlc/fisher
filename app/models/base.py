"""
  Created by lin at 2019-06-11
"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, SmallInteger

db = SQLAlchemy()


class Base(db.Model):
    status = Column(SmallInteger, default=1)
