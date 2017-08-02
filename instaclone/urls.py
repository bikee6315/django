from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.signup_view),
    url('login/',views.login_view),
    url('post/',views.post_view),
    url('feed/',views.feed_view),
    url('like/',views.like_view),
    url('comment/',views.comment_view),


]