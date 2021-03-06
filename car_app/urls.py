from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [


    path('', views.indexView, name="home"),
    path('dashboard/', views.dashboardView, name="dashboard_Url"),
    path('login/', LoginView.as_view(), name="login_url"),
    path('register/', views.registerView, name="register_url"),
    path('checkout/<int:id>',views.checkoutview,name="checkout_url"),
    path('logout/', views.logout, name="logout"),
    path('final/',views.finalView,name="final_url"),


]
