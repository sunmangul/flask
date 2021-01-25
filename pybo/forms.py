from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class QuestionForm(FlaskForm):  # FlaskForm을 상속 받는다(subject, content 속성포함)
    subject = StringField('제목', validators=[DataRequired('필수입력 항목')])  #글자수 제한 StringField 제한X TextAreaField
    content = TextAreaField('내용', validators=[DataRequired('필수입력 항목')])  #에러 메세지 출력


class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('필수입력 항목')])
