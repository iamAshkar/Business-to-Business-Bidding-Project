from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from B2B_App.models import UserType, Customer_Reg, Farmer_Reg


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class Registration(TemplateView):
    template_name = 'user_reg.html'

    def post(self, request, *args, **kwargs):
        fullname = request.POST['name']
        address = request.POST['address']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']

        try:
            user = User.objects.create_user(username=email, password=password, first_name=fullname, email=email,last_name=1)
            user.save()
            reg = Customer_Reg()
            reg.user = user
            reg.address = address
            reg.phonenumber = phone
            reg.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = 'user'
            usertype.save()
            messages = "Register Successfully."

            return render(request, 'index.html', {'message': messages})
        except:
            messages = "Username already used!.."
            return render(request, 'index.html', {'message': messages})



class farmer_reg(TemplateView):
    template_name = 'farmer_registration.html'

    def post(self, request, *args, **kwargs):
        fullname = request.POST['name']
        address = request.POST['address']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']

        try:
            user = User.objects.create_user(username=email, password=password, first_name=fullname, email=email,last_name=0)
            user.save()
            reg = Farmer_Reg()
            reg.user = user
            reg.address = address
            reg.phonenumber = phone
            reg.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = 'farmer'
            usertype.save()
            messages = "waiting for approval."

            return render(request, 'index.html', {'message': messages})
        except:
            messages = "Username already used!.."
            return render(request, 'index.html', {'message': messages})

class Login(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            if user.last_name == '1':
                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "user":
                    return redirect('/user')
                elif UserType.objects.get(user_id=user.id).type == "farmer":
                    return redirect('/farmer')
                # elif UserType.objects.get(user_id=user.id).type == "accounts":
                #     return redirect('/accounts')

            else:
                return render(request, 'login.html', {'message': " User Account Not Authenticated"})


        else:
            return render(request, 'login.html', {'message': "Invalid Username or Password"})
