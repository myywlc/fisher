from flask import current_app, flash, redirect, url_for

from app.models.base import db
from app.models.gift import Gift
from app.spider.yushu_book import YuShuBook
from . import web
from flask_login import login_required, current_user


@web.route('/my/gifts')
@login_required
def my_gifts():
    # uid = current_user.id
    # gifts = Gift.query.filter_by(uid=uid, launched=False).order_by(
    #     desc(Gift.create_time)).all()
    # wishes_count = GiftService.get_wish_counts(gifts)
    # view_model = MyGifts(gifts, wishes_count).package()
    # return render_template('my_gifts.html', gifts=view_model)
    return 'my_gifts'


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            gift = Gift()
            gift.uid = current_user.id
            gift.isbn = isbn
            db.session.add(gift)
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
    else:
        flash('这本书已添加至你的赠送清单或已存在于你的心愿清单，请不要重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/gifts/<gid>/redraw')
@login_required
def redraw_from_gifts(gid):
    pass



