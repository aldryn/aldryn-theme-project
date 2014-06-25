# -*- coding: utf-8 -*-

# Note: this is not used yet, because our setup doesn't work with Celery 3.1 just yet

# from __future__ import absolute_import
#
# import os
#
# from celery import Celery
# from django.conf import settings
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings_local')
#
# app = Celery('core')
# app.config_from_object('django.conf:settings')
# app.autodiscover_tasks(settings.INSTALLED_APPS, related_name='tasks')
