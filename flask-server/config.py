"""Application configuration."""
import os

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin


class BaseConfig:
    """Base configuration."""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # swagger registration
    APISPEC_SPEC = APISpec(
        title='DoList',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    )
    APISPEC_SWAGGER_URL = '/swagger/'
    APISPEC_SWAGGER_UI_URL = '/swagger-ui/'


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEVELOPMENT_DATABASE_URI')


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TESTING_DATABASE_URI')


config = {'development': DevelopmentConfig,
          'testing': TestingConfig,
          'default': DevelopmentConfig}
