from django.urls import path
from .views import signupclass
from .views import ProfileDisplay
#from .views import logoutConfirmation
app_name = 'accounts'

urlpatterns = [
    path('signup/',signupclass.as_view(),name = 'signup_view'),
    path('profile/',ProfileDisplay.as_view() , name = 'Profile_view'),
    #path('logout_confirmation/',logoutConfirmation.as_view(), name = 'logout_confirmation'),
]