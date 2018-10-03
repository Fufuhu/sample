from django.conf.urls import url
from .views.base_view import BaseView

app_name = 'guestbook'

urlpatterns = [
    url(r'^$', BaseView.as_view(), name='base'),
]