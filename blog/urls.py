from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.posts),
	url(r'login', views.index),
	url(r'cadastro', views.cadastro),
	url(r'posts', views.posts),
	url(r'cadAnimais', views.novo_animal),
	url(r'cadBiomas', views.novo_bioma),
	url(r'sobre', views.sobre),
	url(r'^upvote/(?P<post_post_id>[0-9]+)/$', views.upvote, name='upvote')
]