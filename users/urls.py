from django.conf.urls import url, include
from django.urls import path
from users import views

urlpatterns = [
    path('show/', views.user_list),
    path('get/<int:user_id>/' , views.user_get),
    path('add/', views.user_add),
    path('remove/<int:user_id>', views.user_remove),
    path('update/<int:user_id>' , views.user_update),
]