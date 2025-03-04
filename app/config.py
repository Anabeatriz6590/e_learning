class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://user:password@localhost/e_learning"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_URL = "redis://localhost:6379/0"
    CELERY_BROKER_URL = REDIS_URL
    CELERY_RESULT_BACKEND = REDIS_URL

