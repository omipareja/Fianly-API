from django.urls import path
from applications.users.api.views.LoginView import Login

urlpatterns = [

    path('auth/', Login.as_view(), name='token_obtain_pair2'),

]