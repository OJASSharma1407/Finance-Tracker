from django.contrib import admin
from django.urls import path
from user_auth.views import*
from tracker.views import*

urlpatterns = [
    path('',login,name='login'),
    path('reg/',reg,name='reg'),
    path('dashboard/',dashboard,name='dashboard'),
    path('transactions/',transactions,name='transactions'),
    path('add_transaction/',add_transaction,name='add_transaction'),
    path('logout/',user_logout,name='logout'),
    path('admin/', admin.site.urls),
]
