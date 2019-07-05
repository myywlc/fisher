"""
  Created by lin at 2019-06-11
"""
from flask import current_app
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String
from sqlalchemy.orm import relationship
from app.models.base import Base
from app.spider.yushu_book import YuShuBook


class Gift(Base):
    __tablename__ = 'gift'

    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    @classmethod
    def recent(cls):
        recent_gift = Gift.query.filter_by(launched=False).group_by(Gift.book_id).order_by(
            Gift.create_time).limit(current_app.config['RECENT_BOOK_PER_PAGE']).distinct().all()
        return recent_gift
