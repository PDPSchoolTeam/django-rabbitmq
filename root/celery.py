import os
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')

app = Celery('root')

# Konfiguratsiyani django settings.py dan olib kelish # noqa
app.config_from_object('django.conf:settings', namespace='CELERY')

# Avtomatik tasklarni topish # noqa
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')