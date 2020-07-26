from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.models import User
from .LoginAuthentication import EmailAuthentication
from django.contrib.auth import login, logout
from django.core.mail import send_mail

# checks the whether the user is logged in or not
class FirstEntry(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect('signin/')
        return redirect('/blog/')

# create a new user  
class SignUp(View):
    # class view
    def get(self, request, *args, **kwargs):
        return render(request,'Signup.html', {})

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            print(request.POST)
            data = request.POST
            if data['password'] == data['confirmpassword']:
                # creating a new user using User class
                new_user = User.objects.create_user(username=data['username'], email = data['useremail'], password = data['password'])
                new_user.is_active = False
                new_user.first_name = data['firstname']
                new_user.last_name = data['lastname']
                new_user.save()
                return render(request, 'Login.html', {})

            else:
                print('password not matched')
                return render(request,'Signup.html', {})
# sign in the user
class SignIn(View):
    def get(self, request, *args, **kwargs):
        global random_number
        # genetating a random 4 digit OTP code
        random_number = User.objects.make_random_password(length=4, allowed_chars='0123456789')
        return render(request,'Login.html', {})
    def post(self, request, *args, **kwargs):
        
        if request.POST:
            global auth_user
            print(request.POST)
            # print('super User : ', User.objects.filter(is_superuser=True))
            # print('returned auth : ', EmailAuthentication().authenticate(request, email=request.POST['useremail'],password=request.POST['loginpassword']))
            auth_user = EmailAuthentication().authenticate(request, email=request.POST['useremail'],password=request.POST['loginpassword'])
            self.auth_user = auth_user
            if auth_user is not None:
                send_mail(subject = 'Log in OTP code', 
                message= 'Use this OTP code to login.\n'+ random_number, 
                from_email = 'admin@admin.com', 
                recipient_list = [auth_user.email, ] )

            #     abc = login(request, auth_user)
                return redirect('/otpcheck/')
        return render(request, 'Login.html', {})

# check whether the entered number is OTP code or not   
class OtpCheck(SignIn):
    def get(self, request, *args, **kwargs):
        return render(request, 'OTPform.html', {})
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            if random_number == request.POST['otp']:
                print('this is object', auth_user)
                if auth_user is not None:
                    abc = login(request, auth_user)
                    return redirect('/blog/')
            else:
                return render(request, 'Login.html', {})
        return render(request, 'OTPform.html', {})

#  to log out user
def userLogout(request):
    logout(request)
    return redirect('/signin/')

