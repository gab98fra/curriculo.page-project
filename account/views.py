from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import (PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, 
                                        PasswordResetCompleteView)
from account.forms import (LoginForm, CreateUserForm, PasswordResetForm1, PasswordChangeForm1, SetPasswordForm1, 
                    UserDataUpdateForm)


class LoginView(FormView):
    """Login
        
        
        :FormView: django form
    """
    
    template_name="account/login.html"
    form_class=LoginForm
    success_url=reverse_lazy("dashboard")
    
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        
        if request.user.is_authenticated:
        
            return HttpResponseRedirect(self.get_success_url())
        
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


def logoutView(request):
    "Logout"
    
    logout(request)
    return redirect("home:home")


class CreateUserView(CreateView):
    """Add user
        
        
        :CreateView: django view
    """
    
    template_name="account/register.html"
    form_class=CreateUserForm
    
    def post(self, request, *args, **kwargs):

        form=self.form_class(data=request.POST)
        if form.is_valid():
        
            form.save()
            return redirect("done")
        
        else:    
            
            return redirect('/accounts/register/?fail')


class DoneView(TemplateView):
    "Successful registration"

    template_name="account/done.html"


class AccountView(LoginRequiredMixin, ListView):
    """User data
    
    
        :LoginRequiredMixin: mixin django for authentication
        :ListView:django view
    """
    
    model= User
    template_name="account/account.html"
    
class UserDataUpdateView(LoginRequiredMixin, UpdateView):
    """Update user data
        
        
        :UpdateView: django view
    """
    
    model=User
    form_class=UserDataUpdateForm
    context_object_name="form"
    template_name='account/update.html'
    success_url=reverse_lazy("account")

class DeleteUserView(LoginRequiredMixin,DeleteView):
    """Delete User
    
    
       :DeleteView: django view
    """
    model=User
    context_object_name="form"
    template_name='account/delete.html'

    def post(self, request, pk, *args, **kwargs):
        object=self.model.objects.get(id=pk)
        object.is_active=False
        object.save()
        return redirect ("home:home")    

class PassworChangeView(UpdateView):
    "Change user password"

    model=User
    form_class=PasswordChangeForm1
    template_name="account/change.html"
    
    def get(self, request, *args, **kwargs):
        form=self.form_class(user=request.user)
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        form=self.form_class(user=request.user, data=request.POST )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/login/')
        else:    
            return HttpResponseRedirect('/accounts/password_change2/')

class ResetPasswordView(PasswordResetView):
    """Reset user password
        Step 1
        
        
        :PasswordResetView: django view
    """
    
    template_name="account/reset/reset.html"
    form_class=PasswordResetForm1
    from_email="noreply@gmail.com"
    success_url=reverse_lazy("password_reset_done")    

    
class PasswordResetDoneView1(PasswordResetDoneView):
    """Reset user password
        Step 2
        
        
        :PasswordResetDoneView:django view
    """
    
    template_name="account/reset/reset_sent.html"

class PasswordResetConfirmView1(PasswordResetConfirmView):
    """Reset user password
        Step 3
        
        
        :PasswordResetConfirmView:django view
    """
    
    form_class=SetPasswordForm1
    template_name = 'account/reset/confirm.html'
    success_url =reverse_lazy('password_reset_complete')

class PasswordResetCompleteView1(PasswordResetCompleteView):
    """Reset user password
        Step 4
        
        
        :PasswordResetCompleteView:django view
    """
    
    template_name="account/reset/reset_complete.html"
    
