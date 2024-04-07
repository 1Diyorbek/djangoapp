from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import  User


class StudentRegisterView(View):
    def get(self, request):
        return render(request, "auth_templates/register.html")

    def post(self, request):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        username = request.POST["username"]
        password1 = request.POST["password_1"]
        password2 = request.POST["password_2"]

        if password1 == password2:
            user = User(first_name=first_name, last_name=last_name, email=email, username=username, password=password1)
            user.save()

            """User passwordini qo'shisihda oddiy usulda qo'shildi. Chunki login qilinganda password larni 
            birga-bir tekshiriladi. Shu sabab hozircha shu usulda qo'shildi. set_password() metodi orqali
            qo'shsak uni shifrlab qo'yadi va biz uni tekshira olmaymiz. Domla uni djangoning formalar bilan ishlash
            qismini o'tganimda tushuntiraman dedi."""

            return redirect('landing')

        else:
            return redirect('register')


class StudentLoginView(View):
    def get(self, request):
        return render(request, "auth_templates/login.html")

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]

        user = User.objects.filter(username=username, password=password)

        if user:
            return redirect('landing')

        else:
            return redirect('login')
