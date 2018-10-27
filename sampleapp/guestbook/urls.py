from django.conf.urls import url
from .views.base_view import BaseView
from .views.threads_view import ThreadsView
from .views.comments_view import CommentsView

app_name = 'guestbook'

urlpatterns = [
    url(r'^$', BaseView.as_view(), name='base'),
    url(r'^threads/',  ThreadsView.as_view(), name='threads'),
    url(r'^comments/(.+)/$', CommentsView.as_view(), name='comments'),
]