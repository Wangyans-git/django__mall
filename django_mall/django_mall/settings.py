"""
Django settings for django_mall project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '736&nf#)268dx9#c3=tg*#z0s2u!#^8xdt16f=z#5x3x0ljt6^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]    # 所有ip可以访问

# Application definition

# 安装的应用程序
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',    # 富文本编辑器
    'ckeditor_uploader',
    'accounts.apps.AccountsConfig',  # 用户账户模块
    'mall.apps.MallConfig',  # 商品模块
    'mine.apps.MineConfig',  # 个人中心模块
    'system.apps.SystemConfig',  # 系统模块
]

# 中间件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'utils.middleware.ip_middleware',
    # 'utils.middleware.MallAuthMiddleware',
]

ROOT_URLCONF = 'django_mall.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,  # 开启就是在各自文件中的template中查找
        'OPTIONS': {
            'context_processors': [         # 上下文处理器
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'system.context_processors.count',
                'mine.context_processors.shop_cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_mall.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'django_mall',
            'USER': 'root',
            'PASSWORD': 'admin123',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            # 'OPTIONS': {'init_command':"SET foreign_key_checks = 0;",}
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# 静态文件路径
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# 自己上传的图片
MEDIA_URL = '/medias/'
MEDIA_ROOT = os.path.join(BASE_DIR,'medias')

# 使用自定义的用户模型
AUTH_USER_MODEL = 'accounts.User'
LOGIN_URL = '/accounts/user/login/'


CKEDITOR_UPLOAD_PATH = os.path.join(MEDIA_ROOT,'uploads')

# 异步的CSRF
CSRF_USE_SESSIONS = False

# 邮件配置
EMAIL_HOST = 'smtp.qq.com'
EMAIL_HOST_USER = '951772384@qq.com'
EMAIL_HOST_PASSWORD = 'mnmllbyoypwbbfah'

SERVER_EMAIL = '951772384@qq.com'
ADMINS = [('admin','951772384@qq.com')]

# 日志的配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'sql_log_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'log/sql.log'),
        },
        'log_index_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(BASE_DIR, 'log/index.log'),
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            # 'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            # 'filters': ['special']
        }
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['sql_log_file',],
            'level': 'DEBUG',
            'propagate': True,
        },
        'index': {
            'handlers': ['log_index_file', 'console'],
            'level': 'DEBUG',
        }
    },
}