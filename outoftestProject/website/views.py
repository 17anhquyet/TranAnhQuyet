from django.shortcuts import redirect, render
from .models import Customer
from .forms import CustomerForm
from django.contrib import messages

# Create your views here.
def home(request):
    Customers = Customer.objects.all()
    return render(request,'home.html',{'Customers':Customers})

def signup(request):
    if request.method == "POST":
        form = CustomerForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,'Your form is completed')
            return redirect('home')
        else:
            name = request.POST['name']
            age = request.POST['age']
            email = request.POST['email']
            messages.success(request,'Your form is failed')
            return render(request,'signup.html',{
                'name':name,
                'age':age,
                'email':email
            })
        
    else:
        return render(request,'signup.html',{})