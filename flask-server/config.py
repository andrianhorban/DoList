"""Application configuration."""
import os


class BaseConfig:
    """Base configuration."""
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEVELOPMENT_DATABASE_URI')


class TestingConfig(BaseConfig):
    """Testing configuration."""
    pass


config = {'development': DevelopmentConfig,
          'testing': TestingConfig,
          'default': DevelopmentConfig}
