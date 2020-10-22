from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class BookForm(FlaskForm):
    name = StringField('姓名', validators=[DataRequired()])
    college = StringField('学院', validators=[DataRequired()])
    stu_num = StringField('学号', validators=[DataRequired()])
    qq = StringField('qq', validators=[DataRequired()])
    phone = StringField('联系方式', validators=[DataRequired()])
    detail = StringField('简述问题', validators=[DataRequired()])
    submit = SubmitField("预约")

# defination
name = None
college = None
stu_num = None
qq = None
phone = None
detail = None