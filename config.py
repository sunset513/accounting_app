import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'your_secret_key'  # 請使用環境變數或其他方式保護密鑰
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'accounting.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
