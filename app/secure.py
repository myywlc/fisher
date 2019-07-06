"""
  Created by lin at 2019-06-08
"""

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:@localhost/fisher'

SECRET_KEY = '\x88D\xf09\x91\x07\x98\x89\x87\x96\xa0A\xc68\xf9\xecJ:U\x17\xc5V\xbe\x8b\xef\xd7\xd8\xd3\xe6\x98*4'

SQLALCHEMY_TRACK_MODIFICATIONS = False

# Email 配置
MAIL_SERVER = 'smtp.exmail.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = 'hello@yushu.im'
MAIL_PASSWORD = 'Bmwzy1314520'
MAIL_SUBJECT_PREFIX = '[鱼书]'
MAIL_SENDER = '鱼书 <hello@yushu.im>'
