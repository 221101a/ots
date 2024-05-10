from django.urls import path
from online_test import views
app_name='user'
urlpatterns = [
    path("welcome",views.welcome,name='welcome'),
    path("signup",views.signup,name='signup'),
    path("store_user",views.store_user,name='store_user'),
    path("login",views.login,name='login'),
    path("homepage",views.homepage,name='homepage'),
    path("subject1",views.subject1,name='subject1'),
    path("subject2",views.subject2,name='subject2'),
    path("subject3",views.subject3,name='subject3'),
    path("result1",views.result1,name='result1'),
    path("result2",views.result2,name='result2'),
    path("result3",views.result3,name='result3'),
    path("profile",views.profile,name='profile'),
    path("profile_save",views.profile_save,name='profile_save'),
    path("test_history",views.test_history,name='test_history'),
    path("logout",views.logout,name='logout'),
    path("aboutUs",views.aboutUs,name='aboutUs'),
]