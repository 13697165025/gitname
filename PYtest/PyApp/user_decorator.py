from django.http import HttpResponseRedirect

# 登录验证

def Login(func):
    def login_fun(request, *args, **kwargs):
        if request.session.has_key('user_id'):
            return func(request, *args, **kwargs)
        else:
            red = HttpResponseRedirect('/Login/')
            red.set_cookie('url', request.get_full_path())
            return red
    return login_fun



"""
request.path() ：为当前路径
request.get_full_path():为完整路径
"""
