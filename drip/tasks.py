from celery import task
from drip.models import Drip

@task()
def send_drips():
    for drip in Drip.objects.filter(enabled=True):
        drip.drip.run()
