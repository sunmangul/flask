# 환경변수, 데이터베이스 설정을 추가하는 파일
import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))  # 데이터 베이스 직접주소
SQLALCHEMY_TRACK_MODIFICATIONS = False  # sqlalchemy의 이벤트 처리 옵션(파이보에서 사용하지 않음)

SECRET_KEY = "dev"