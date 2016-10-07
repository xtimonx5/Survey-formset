from django.http import request, HttpResponse
from django.shortcuts import render

# Create your views here.


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.shortcuts import render_to_response
from django.contrib import auth
from django.views.generic import FormView, TemplateView, View
from django.contrib.auth.models import User


class LoginView(FormView):
    model = auth.get_user_model()
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = '/'

    def form_valid(self, form):
        usr = self.request.POST.get('username')
        pas = self.request.POST.get('password')
        user = auth.authenticate(username=usr, password= pas)
        context={
        }
        if user is not None:
            auth.login(self.request, user)
        else:
            context= {'login_error', 'UserNotFound'}
        return render_to_response('questionnaire/thanks.html', context)



class RegisterView(FormView):
    model = auth.get_user_model()
    template_name = 'register.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        context={}
        username=self.request.POST.get('username')
        email=self.request.POST.get('email')
        pass1=self.request.POST.get('password1')
        pass2=self.request.POST.get('password2')
        if (pass1==pass2):
            user=User.objects.create_user(username,email,pass2)
            new_user= auth.authenticate(username=username, password=pass2)
            auth.login(self.request, new_user)
        else:
            context= {'login_error', 'dnische'}
        return render_to_response('questionnaire/thanks.html', context)

class LogOutView(View):
    template_name = 'login.html'
    def get(self, url):
        auth.logout(self.request)
        return render_to_response('questionnaire/thanks.html')


def logout(request):
    auth.logout(request)
    return render('questionnaire/thanks.html')
