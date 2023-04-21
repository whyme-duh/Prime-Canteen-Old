from email import message
from multiprocessing import context

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from Users.forms import ProfileUpdateForm, UserRegistrationForm, UserUpdateForm

# Create your views here.

def registration(request):
	if request.method == "POST":
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f'Your account has been created so please login.' )
			return redirect('login')
		else:
			messages.error(request, f'Details are not correct' )
	else:

		form = UserRegistrationForm()
	return render(request , 'users/register.html', {'form' : form})



@login_required
def profile(request):
	if request.method == "POST":
		userUpdate = UserUpdateForm(request.POST, instance = request.user)
		profileUpdate = ProfileUpdateForm(request.POST,instance=request.user.profile)
		if userUpdate.is_valid() and profileUpdate.is_valid():
			userUpdate.save()
			profileUpdate.save()
			messages(request, f'Your profile has been updated')
			return redirect('user-profile')
		else:
			messages.error(request, f'Failed!!')
	else:
		userUpdate = UserUpdateForm(instance=request.user)
		profileUpdate = ProfileUpdateForm(instance = request.user.profile)
	context = {
		'userUpdate_form' :userUpdate,
		'profileUpdate_form' : profileUpdate
	}
	return render(request, 'users/profile.html', context)
