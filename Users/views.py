from django.shortcuts import render,redirect         
from django.contrib import messages                            
from django.contrib.auth.decorators import login_required 
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()                                                                     # saves the data from the form
            username = form.cleaned_data.get('username')                                    # retrives the data of username
            messages.success(request, f'Account has been created { username }! ')           # sends messages as toaster
            return redirect('login')                                                        # redirecting the page to Blog-home
    else:
        form = UserRegistrationForm()
    return render(request, 'Users/register.html', { 'form': form } )

