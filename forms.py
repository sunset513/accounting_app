from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange

class TransactionForm(FlaskForm):
    date = DateField('日期', format='%Y-%m-%d', validators=[DataRequired()])
    description = StringField('描述', validators=[DataRequired(), Length(max=200)])
    category = SelectField('類別', choices=[
        ('收入', '收入'),
        ('食物', '食物'),
        ('交通', '交通'),
        ('娛樂', '娛樂'),
        ('其他', '其他')
    ], validators=[DataRequired()])
    amount = FloatField('金額', validators=[DataRequired(), NumberRange(min=0.01)])
    submit = SubmitField('提交')
