"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from datetime import timedelta
from pathlib import Path
from django.conf import settings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-&5^0nz@l+d-*2m)m^$m!g-1xu#*kcahlk%3riryn&ocyg=&%gg"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'blog',
    'blog_api',
    'rest_framework',
    'corsheaders',
    'users',
    'rest_framework_simplejwt.token_blacklist',
    'drf_yasg',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'your_project.middleware.NoRedirectMiddleware',
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [BASE_DIR / 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8000",

]
# CORS_ORIGIN_ALLOW_ALL = False
# CORS_ORIGIN_WHITELIST = [
#     "https://example.com",
#     "https://sub.example.com",
#     "http://localhost:8080",
#     "http://127.0.0.1:9000"
# ]
# CORS_ALLOW_ORIGINS = ['*']
# CORS_ALLOW_METHODS = (
#     "DELETE",
#     "GET",
#     "OPTIONS",
#     "PATCH",
#     "POST",
#     "PUT",
# )


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],

    # 'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']

}
SWAGGER_SETTINGS = {
    'SHOW_REQUEST_HEADERS': True,
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },
    'USE_SESSION_AUTH': False,
    'JSON_EDITOR': True,
    'SUPPORTED_SUBMIT_METHODS': [
        'get',
        'post',
        'put',
        'delete',
        'patch'
    ],
}
# Custom user model
AUTH_USER_MODEL = "users.NewUser"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,

    "ALGORITHM": "HS256",
    "SIGNING_KEY": settings.SECRET_KEY,
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,

    "AUTH_HEADER_TYPES": ("Bearer", "JWT"),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",

    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}
"""
AllowAny
The AllowAny permission class will allow unrestricted access, regardless of if the request was authenticated or unauthenticated.

This permission is not strictly required, since you can achieve the same result by using an empty list or tuple for the permissions setting, but you may find it useful to specify this class because it makes the intention explicit.

IsAuthenticated
The IsAuthenticated permission class will deny permission to any unauthenticated user, and allow permission otherwise.

This permission is suitable if you want your API to only be accessible to registered users.

IsAdminUser
The IsAdminUser permission class will deny permission to any user, unless user.is_staff is True in which case permission will be allowed.

This permission is suitable if you want your API to only be accessible to a subset of trusted administrators.

IsAuthenticatedOrReadOnly
The IsAuthenticatedOrReadOnly will allow authenticated users to perform any request. Requests for unauthorised users will only be permitted if the request method is one of the "safe" methods; GET, HEAD or OPTIONS.

This permission is suitable if you want to your API to allow read permissions to anonymous users, and only allow write permissions to authenticated users.
"""


"""
File này chứa cấu hình cho thư viện Django Simple JWT (JSON Web Token). Dưới đây là một số giải thích về các cấu hình trong file:

ACCESS_TOKEN_LIFETIME: Định thời gian tồn tại (lifetime) của access token.

REFRESH_TOKEN_LIFETIME: Định thời gian tồn tại (lifetime) của refresh token.

ROTATE_REFRESH_TOKENS: Xác định liệu refresh token có được xoay vòng hay không.

BLACKLIST_AFTER_ROTATION: Xác định liệu access token được đưa vào danh sách đen sau khi refresh token xoay vòng hay không.

UPDATE_LAST_LOGIN: Xác định liệu trường last_login của người dùng sẽ được cập nhật sau khi tạo access token hay không.

ALGORITHM: Xác định thuật toán mã hóa JWT, trong trường hợp này là HS256.

SIGNING_KEY: Khóa bí mật được sử dụng để ký và xác minh JWT. Trong trường hợp này, nó lấy giá trị từ settings.SECRET_KEY của Django.

VERIFYING_KEY: Khóa công khai được sử dụng để xác minh chữ ký JWT.

AUDIENCE: Xác định khán giả (audience) cho JWT.

ISSUER: Xác định người phát hành (issuer) của JWT.

JSON_ENCODER: Serializer JSON sử dụng để mã hóa và giải mã JWT.

JWK_URL: Đường dẫn URL để tải JSON Web Key (JWK).

LEEWAY: Khoảng thời gian phụ (leeway) được áp dụng khi xác minh hạn chế thời gian của JWT.

AUTH_HEADER_TYPES: Danh sách các loại header sẽ được xem là phần header chứa access token.

AUTH_HEADER_NAME: Tên header HTTP chứa access token.

USER_ID_FIELD: Trường trong model người dùng sẽ được sử dụng làm trường xác định người dùng trong JWT.

USER_ID_CLAIM: Trường trong JWT chứa thông tin xác định người dùng.

USER_AUTHENTICATION_RULE: Quy tắc xác thực người dùng mặc định sẽ được áp dụng.

AUTH_TOKEN_CLASSES: Danh sách các lớp token được sử dụng để tạo và xác minh token.

TOKEN_TYPE_CLAIM: Trường trong JWT để xác định loại token (access hoặc refresh).

TOKEN_USER_CLASS: Lớp mô hình người dùng được sử dụng trong JWT.

JTI_CLAIM: Trường trong JWT chứa thông tin về JWT ID (JTI).

SLIDING_TOKEN_REFRESH_EXP_CLAIM: Trường trong JWT chứa thông tin hạn chế thời gian của sliding token refresh.

SLIDING_TOKEN_LIFETIME: Định thời gian tồn tại (lifetime) của sliding token.

SLIDING_TOKEN_REFRESH_LIFETIME: Định thời gian tồn tại (lifetime) của sliding token refresh.

TOKEN_OBTAIN_SERIALIZER: Serializer được sử dụng khi tạo access token.

TOKEN_REFRESH_SERIALIZER: Serializer được sử dụng khi làm mới access token.

TOKEN_VERIFY_SERIALIZER: Serializer được sử dụng khi xác minh access token.

TOKEN_BLACKLIST_SERIALIZER: Serializer được sử dụng để thêm access token vào danh sách đen.

SLIDING_TOKEN_OBTAIN_SERIALIZER: Serializer được sử dụng khi tạo sliding token.

SLIDING_TOKEN_REFRESH_SERIALIZER: Serializer được sử dụng khi làm mới sliding token.

Các cấu hình này cho phép bạn tùy chỉnh hành vi và tính năng của Django Simple JWT theo yêu cầu của dự án của bạn. Bạn có thể điều chỉnh các giá trị này để thay đổi thời gian tồn tại của token, cách mã hóa, cách xác thực, và các yếu tố khác của JWT.
"""
