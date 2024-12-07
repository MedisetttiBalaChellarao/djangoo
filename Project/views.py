from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404



# Create your views here.
def projecthomepage(request):
    return render(request, 'ProjectHomePage.html')

from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render
def UserRegisterPageCall(request):
    return render(request, 'Project/UserRegisterPage.html')
def UserRegisterLogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'Project/UserRegisterPage.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'Project/UserRegisterPage.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'Project/Projecthomepage.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'Project/UserRegisterPage.html')
    else:
        return render(request, 'Project/UserRegisterPage.html')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


def UserLoginPageCall(request):
    return render(request, 'Project/loginpage.html')

from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth import authenticate

def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if len(username) == 10:
                # Redirect to StudentHomePage
                messages.success(request, 'Login successful as student!')
                return redirect('Customer:CustomerHomePage')  # Replace with your student homepage URL name
                #return render(request, 'studentapp/StudentHomepage.html')
            elif len(username) >= 4:
                # Redirect to FacultyHomePage
                messages.success(request, 'Login successful as faculty!')
                return redirect('Restaurant:RestaurantHomePage')  # Replace with your faculty homepage URL name
                #return render(request, 'facultyapp/FacultyHomepage.html')
            else:
                # Invalid username length
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'Project/loginpage.html')
        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')
            return render(request, 'Project/loginpage.html')
    else:
        return render(request, 'Project/loginpage.html')


def logout(request):
    auth.logout(request)
    return redirect('projecthomepage')

def payment(request):
    return render(request, 'Customer/payment.html')