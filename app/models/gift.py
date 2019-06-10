"""
  Created by lin at 2019-06-11
"""

from sqlalchemy import Column, Integer, Boolean, ForeignKey, String
from sqlalchemy.orm import relationships
from app.models.base import Base


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationships('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)
