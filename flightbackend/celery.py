""" Celery configuration """
from __future__ import absolute_import

import os

from celery import Celery
from django.conf import settings

# pylint: disable=invalid-name
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flightbackend.settings')
app = Celery('flight_backend')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug(self):
    """ debug """
    print('Request: {0!r}'.format(self.request))
