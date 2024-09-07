from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')  # Automatically log the user in after registration
            messages.success(request, 'Registration successful.')
            return redirect('items/phone')  # Redirect to the homepage or another page after registration
    else:
        form = UserCreationForm()
    return render(request, 'account/register.html', {'form': form})