# 화면을 구성하는 파일
from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')  # 이름, 모듈명, URL 프리픽스값 전달


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
def index():
    return redirect(url_for('question._list'))
    # 입력받은 URL로 리다이렉트 해주고, 라우트가 설정된 함수명으로 URL을 역으로 찾아준다.
    # 리다이렉트 기느으로 localhost:5000/question/list/ 자동호출