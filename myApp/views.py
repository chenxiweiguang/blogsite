from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def test(request):
    return HttpResponse("Wellcome to my blogsite!")
def test1(request):
    return render(request, 'myApp/test1.html', )
def index(request):
# 去模板里取数据
# gradesList = Grades.objects.all()
# 将数据传递给模板,模板再渲染页面，将渲染好的页面返回给浏览器
    return render(request, 'myApp/index.html', )
def about(request):
    return render(request, 'myApp/about.html', )
def gbook(request):
    return render(request, 'myApp/gbook.html', )
def learn(request):
    return render(request, 'myApp/learn.html', )
def mbfx(request):
    return render(request, 'myApp/mbfx.html', )
def manshenghuo(request):
    return render(request, 'myApp/manshenghuo.html', )

import os
import django
os.environ.setdefault('DJANGO_SETTING_MODULE', 'blogsite.settings')
django.setup()

from myApp.models import blogUser
def register(request):
    if request.method=="GET":
        data={
            "title":"注册"
        }
        return render(request, 'myApp/user/register.html',context=data )
    elif request.method=="POST":
        name=request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        icon = request.FILES.get("icon")
        user=blogUser()
        user.username=name
        user.useremail=email
        user.userpassword = password
        user.usericon = icon
        user.save()
        return redirect('/singin/')


from captcha.fields import CaptchaField

def singin(request):
    if request.method=="GET":
        data={
            "title":"登录",
        }


        return render(request, 'myApp/user/singin.html',context=data )
    elif request.method=="POST":
        name=request.POST.get("name")
        password = request.POST.get ("password")

        if name and password:
            try:
                users = blogUser.objects.get(username=name)
                if users.userpassword==password:
                    message=name
                    return render(request, 'myApp/index.html', {"message": message})
                    # return HttpResponse("登录成功")
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！"
        else:
            message = "用户名和密码不能为空！"
        return render(request,'myApp/user/singin.html', {"message": message})
def singout(request):
    return redirect('/index/')













# 重定向
from django.shortcuts import redirect
def index1(request):
    return redirect('/index')