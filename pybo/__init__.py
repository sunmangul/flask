# 주로 main.py로 쓰일 파일(돌아가는 곳)
from flask import Flask  # import 다들 아는 그거
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()   # 객체를 create_app에서 생성하면 다른 모듈에서 사용불가
migrate = Migrate()  # 따라서 생성은 전역, 선언은 create_app함수에서 함


def create_app():
    app = Flask(__name__)  # 애플리케이션 실행(__name__에는 변수명 즉, __init__이 담김)
    app.config.from_object(config)  # config.py를 app.config에 환경변수로 부르기 위한 코드

    #ORM
    db.init_app(app)
    migrate.init_app(app, db)

    from . import models

    # 블루프린트
    from .views import main_views, question_views, answer_views
    app.register_blueprint(main_views.bp)  # views.py에서 경로에 맞게 지정해주고 이렇게 import해와서 사용가능하게 함
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    return app

