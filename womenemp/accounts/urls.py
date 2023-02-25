from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.user_login,name='login'),
    path('reg/',views.reg,name='reg'),
    path('ticket-book/',views.ticket_book,name='ticket-book'),
    path('payment/',views.payment,name='payment'),
    path('userpro/',views.userprofile,name='userpro'),
    path('admindash/',views.admin,name='admin'),
    path('bus/',views.bus,name='bus'),
    path('house/',views.house,name='house'),
    path('revenue/',views.revenue,name='revenue'),
    path('admlogin/',views.user_login1,name='log'),
]