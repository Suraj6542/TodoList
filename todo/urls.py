from django.contrib import admin
from django.urls import path
from todo import views
from .views import index, remove, update

urlpatterns = [
   

    path('', views.index, name="todo"),

    
    path('del/<str:item_id>', views.remove, name="del"),

    path('update/<str:item_id>', views.update, name="update"),

    path('admin/', admin.site.urls),
]
