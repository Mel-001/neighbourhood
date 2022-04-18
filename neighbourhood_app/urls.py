from django.urls import path
from . import views
from django.conf import settings


urlpatterns=[
    path('',views.home,name='home'),
    
    path('search/',views.project,name='search_results'),
    path('business/',views.view_profile,name='business_results'),
    path('new/business/', views.search_project, name='new-business'),
    path('new/post/', views.new_project, name='new-post'),
    path('accounts/profile/', views.ProfileList.as_view(),name='profile'),
    
]
