
from django.urls import path
from .views import snippet_list , snippet_obj


urlpatterns = [

# path('',home,name='home'),
path('snippet-list/',snippet_list,name='snippet_list'),

path('snippet-obj/<int:pk>/',snippet_obj,name='snippet_obj')


]
