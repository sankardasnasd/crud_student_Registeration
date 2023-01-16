from django.shortcuts import render,redirect
from django.http import HttpResponse
from crud_app.forms import Studentform,Students

# Create your views here.
def crud_app(request):
    return render(request,'crud_app')

def create(request):
    form = Studentform()
    
    a = Students.objects.all()
    if request.method == 'POST':
        form = Studentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create')
    return render(request,'create.html',{'form': form,'a':a})



#6. creating update

def update(request,id):
    b = Students.objects.get(id = id)
    form = Studentform(instance=b)

    #7. redirecting update page or filter
    if request.method =='POST':
        form=Studentform(request.POST,instance = b)
        if form.is_valid():
         form.save()
         return redirect('create')
        

    return render(request,'update.html',{'form':form})


# delete
def delete(request,id):
    Students.objects.get(id = id).delete()
    return redirect('create')
def signup(request):
   
    return render(request,'signup.html')

def login(request):
    return render(request,'login.html')

    
