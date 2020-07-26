from django.urls import path
from .views import SignUp, SignIn, FirstEntry, userLogout, OtpCheck

urlpatterns = [
    path('signup/', SignUp.as_view()),
    path('signin/', SignIn.as_view()),
    path('', FirstEntry.as_view()),
    path('logout/', userLogout),
    path('otpcheck/', OtpCheck.as_view()),
]