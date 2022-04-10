from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:article_id>', views.detail, name = 'detail'),
    path('fire/', views.fire, name = 'fire'),
    path('water/', views.water, name = 'water'),
    path('air/', views.air, name = 'air'),
    path('earth/', views.earth, name = 'earth'),
    path('statia/', views.statia, name = 'statia'),
]
