from django.contrib import admin
from ..models import Exercise

from . import logging
from . import workout

admin.site.register(Exercise)
