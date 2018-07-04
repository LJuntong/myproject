from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .. models import Ht
from django.contrib.auth.hashers import make_password, check_password


def index(request):
    

    return render(request,'myadmin/index.html')



def registers(request):
    nexturl = request.GET.get('next','/')
    if request.method =='GET':

        return render(request,'myadmin/register.html')
    elif request.method == 'POST':
        # 执行登录
        # 根据用户名先获取用户对象，再检测密码是否正确
        # try:

        ob = Ht.objects.get(username = request.POST['username'])
        # 验证密码是否正确
        res = check_password(request.POST['password'],ob.password)
        
        if res:
            # 密码正确
            request.session['AdminLogin'] = {'uid':ob.id,'username':ob.username}
            return HttpResponse('<script>alert("登录成功");location.href="/myadmin/"</script>')
        # except:
        #     # 用户名错误
        #     pass
        # return HttpResponse('<script>alert("用户名或密码错误");history.back(-1)</script>')


    # return render(request,'myadmin/register.html')