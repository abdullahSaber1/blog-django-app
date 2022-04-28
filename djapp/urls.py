from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('show/<st_id>', views.show, name='show'),
    path('destroy/<st_id>', views.destroy, name="destroy"),
    path('add/', views.addStudent, name='add'),
    path('edit/<st_id>', views.editStudent, name='edit'),

    # rest_framework

    path('api-all/', views.api_all_student, name='api-all'),
    path('api-one/<st_id>', views.api_one_student, name='api-one'),
    path('api-add/', views.api_add_student, name='add-one'),
    path('api-edit/<st_id>', views.api_edit_student, name='api-edit'),
    path('api-delete/<st_id>', views.api_delete_student, name='api-delete'),


    # auth urls

    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),





]
