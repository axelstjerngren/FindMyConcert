from django.shortcuts import render
from django.http import HttpResponse
from concert.forms import RegistrationForm

def index(request):
	return render(request, 'concert/index.html')

def register(request):
	'''registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			profile.save()
			registered = True
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request, 'concert/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})'''

	if request.method == 'POST':
		form = RegistrationForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('concert/account')
		else:
			form = RegistrationForm()

			args = {'form': form}
			return render(request, 'concert/accounts/registration_form.html', args)


def about(request):
	return render(request, 'concert/about.html')


def faq(request):
	return render(request, 'concert/faq.html')


def contact(request):
	return render(request, 'concert/contact.html')

def myEvents(request):
	return render(request, 'concert/myEvents.html')


