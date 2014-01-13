from django.conf.urls import *
from django.contrib.auth.decorators import login_required

from social_friends.views import FriendListView


urlpatterns = patterns('social_friends.views',
    url(r'^list/$', login_required(FriendListView.as_view()), name='friend_list'),
    url(r'^list/(?P<provider>[\w.@+-]+)/$', login_required(FriendListView.as_view()), name='friend_list'),
)
