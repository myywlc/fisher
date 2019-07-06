from flask import flash, redirect, url_for, render_template, request
from flask_login import current_user

from app.models.gift import Gift
from . import web


@web.route('/drift/<int:gid>', methods=['GET', 'POST'])
def send_drift(gid):
    current_gift = Gift.query.get_or_404(gid)
    if current_gift.is_yourself_gift(current_user.id):
        flash('这本书是你自己的^_^, 不能向自己索要书籍噢')
        return redirect(url_for('web.book_detail', isbn=current_gift.isbn))
    can = current_user.can_satisfied_wish()
    if not can:
        return render_template('not_enough_beans.html', beans=current_user.beans)
    drift_form = DriftForm(request.form)
    if request.method == 'POST':
        if drift_form.validate():
            DriftService.save_a_drift(drift_form, current_gift)
            return redirect(url_for('web.pending'))
    gifter = current_gift.user.summary
    return render_template('drift.html', gifter=gifter, user_beans=current_user.beans, form=drift_form)


@web.route('/pending')
def pending():
    pass


@web.route('/drift/<int:did>/reject')
def reject_drift(did):
    pass


@web.route('/drift/<int:did>/redraw')
def redraw_drift(did):
    pass


@web.route('/drift/<int:did>/mailed')
def mailed_drift(did):
    pass
