# 질문에 관한 링크를 관리하고 내용을 보여주는 파일
from datetime import datetime

from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect

from .. import db
from ..models import Question
from ..forms import QuestionForm, AnswerForm

bp = Blueprint('question', __name__, url_prefix='/question') # 이름, 모듈명, URL 프리픽스값 전달


@bp.route('/list/')
def _list():
    question_list = Question.query.order_by(Question.create_date.desc())  # 질문을 목록으로 생성 [asc/desc]
    return render_template('question/question_list.html', question_list=question_list)  # render_template 함수는 템플릿 파일을 화면에 그림


@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)  # quesiton에 question_id를 조회해서 나오는 DB내용을 넣음+404상황에는 404페이지를 띄움
    return render_template('question/question_detail.html', question=question, form=form)


@bp.route('/create/', methods=('GET', 'POST'))  #전송 방식이 GET인지 POST인지에 따라 달리 처리
def create():
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(subject=form.subject.data, content=form.content.data, create_date=datetime.now())
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('question/question_form.html', form=form)  # form 객체는 템플릿에서 라벨이나 입력 폼 등을 만들 때 사용
