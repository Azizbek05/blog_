from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser, CodeConfirmation
from django.http import HttpResponse
from .decorators import authenticated
from helpes import send_sms, random_code


@authenticated
def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('First name')
        last_name = request.POST.get('Last name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        ex_user = CustomUser.objects.filter(email=email).first()
        if ex_user:
            return HttpResponse("<h1>Bu user ushbu email orqali oldin ro'yhatdan o'tilgan</h1>")
        elif password2 != password1:
            return HttpResponse("<h1>Parollarni to'g'ro kiriting</h1>")
        else:
            user = CustomUser.objects.create_user(
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password2
            )

            code = random_code.generate_code()
            send_sms.send_email(email, code)
            CodeConfirmation.objects.create(
                user=user,
                code=code
            )
            return redirect('verify')

    return render(
        request=request,
        template_name='auth/register.html'
    )

@authenticated
def log_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password1')
        user = authenticate(request=request, email=email, password=password)
        if user:
            login(request=request, user=user)
            return redirect('index')
        else:
            return HttpResponse("<h1>Email yoki password xato</h1>")
    return render(
        request=request,
        template_name='auth/login.html'
    )


def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')

def verify(request):
    email = request.POST.get('email')
    code = request.POST.get('number')
    user = CustomUser.objects.filter(email=email).first()
    if user:
        obj = CodeConfirmation.objects.filter(user=user, code=code).first()
        if obj:
            user.is_active = True
            user.save()
            login(request, user)
            obj.delete()
            return redirect('index')
        return HttpResponse('Email yoki kelgan kod notogri')
    return render(request=request,template_name='auth/code_conf.html')
