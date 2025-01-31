from flask import Flask, render_template, redirect, url_for, flash
from config import Config
from models import db, Transaction
from forms import TransactionForm
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    transactions = Transaction.query.order_by(Transaction.date.desc()).all()
    total = sum(t.amount for t in transactions if t.category == '收入') - sum(t.amount for t in transactions if t.category != '收入')
    return render_template('index.html', transactions=transactions, total=total)

@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    form = TransactionForm()
    if form.validate_on_submit():
        transaction = Transaction(
            date=form.date.data,
            description=form.description.data,
            category=form.category.data,
            amount=form.amount.data
        )
        db.session.add(transaction)
        db.session.commit()
        flash('交易已新增!', 'success')
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

@app.route('/edit/<int:transaction_id>', methods=['GET', 'POST'])
def edit_transaction(transaction_id):
    transaction = Transaction.query.get_or_404(transaction_id)
    form = TransactionForm(obj=transaction)
    if form.validate_on_submit():
        transaction.date = form.date.data
        transaction.description = form.description.data
        transaction.category = form.category.data
        transaction.amount = form.amount.data
        db.session.commit()
        flash('交易已更新!', 'success')
        return redirect(url_for('index'))
    return render_template('edit.html', form=form, transaction=transaction)

@app.route('/delete/<int:transaction_id>', methods=['POST'])
def delete_transaction(transaction_id):
    transaction = Transaction.query.get_or_404(transaction_id)
    db.session.delete(transaction)
    db.session.commit()
    flash('交易已刪除!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
