from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(req):
    return render(req,'home.html')
def about(req):
    return render(req,'about.html')
# def form(req):
#     return render(req,'form.html')




# forms
from django.shortcuts import render, redirect
from .forms import SignInForm

def form(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        # print("==",form)
        if form.is_valid():
            # Process the form data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username)
            print(password)
            # password = form.cleaned_data['wq']
            # You can perform authentication here or redirect to another view
            return redirect('form')
    else:
        form = SignInForm()
    return render(request, 'form.html', {'form': form})


