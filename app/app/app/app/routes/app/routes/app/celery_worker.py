from celery import Celery
from config import Config

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=Config.CELERY_RESULT_BACKEND,
        broker=Config.CELERY_BROKER_URL
    )
    celery.conf.update(app.config)
    return celery