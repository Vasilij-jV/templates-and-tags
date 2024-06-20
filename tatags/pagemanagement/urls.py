from django.urls import path
from .views import *

app_name = 'pagemanagement'

urlpatterns = [
    path('', list_variables, name='list_variables'),
    path('listpages/', list_pages, name='list_pages'),
    path('listpages/<slug:page>/', edit_page, name='one_page'),
    path('listpages/<slug:page>/edit', edit_page, name='edit_page'),
    path('random-color/', random_color_view, name='random_color'),
]
