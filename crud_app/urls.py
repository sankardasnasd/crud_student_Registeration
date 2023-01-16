from django.urls import path
from.import views
from crud_app.views import update
urlpatterns = [
    path('crud_app',views.crud_app),  
   
    path('create',views.create,name = 'create'),

    path('update/<int:id>/',views.update,name='update'),

    path('delete/<int:id>',views.delete,name='delete'),
    path('signup',views.signup,name='signup'),
    
    path('login',views.login,name='login'),
    
]