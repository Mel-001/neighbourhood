from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
   path('',views.home, name='home'),
   path('logout/', views.logoutUser, name='logout'),
   path('profile/',views.profile,name = 'profile'),
   path('comment/<int:id>/',views.comment,name='comment'),
   path('newpost/',views.new_post,name='newpost'),
   path('post/<int:id>/',views.post,name='post'),
   path('search/',views.search_results,name = 'search_results'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)