from django.shortcuts import render, redirect
from django.contrib.auth import (
	authenticate,
	login,
	logout,
	get_user_model
	)
from django.contrib.auth.models import Group
from .forms import LoginForm, Register_Form

User = get_user_model()
# Create your views here.
def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        try:
            login(request,user)
            return redirect('/auth/check/')
        except:
            return redirect('/auth/login')
    context = {
        'form': form
    }
    return render(request,'login.html',context)





def check(request):
	grp = request.user.groups.get()
	user_group = Group.objects.get(name='superuser')
	if grp==user_group:
		return redirect('/superuser/')
	else:
		return redirect('/dash/')






def help_(request):
	logout(request)
	return redirect('/auth/login')






def sign_view(request):
	#i have to register user with group here first
	form = Register_Form(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		confirm_password = form.cleaned_data.get('confirm_password')
		if password == confirm_password:
			user.set_password(password)
			user.save()
			user_group = Group.objects.get(name='user')
			user.groups.add(user_group)
			try:
				user = authenticate(username = username, password = password)
				login(request,user)
				usr = User.objects.get(username=request.user)
				print(usr.groups.get())
			except:
				print('not good')


			return redirect('/')
	context = {
	'form':form
	}
	return render(request,'sign_up.html',context)
