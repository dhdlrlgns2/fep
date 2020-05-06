from django.shortcuts import render
from .models import Todo
from .forms import TodoForm
from django.utils import timezone
# Create your views here.

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def submit(request):
    form = TodoForm()
    return render(request,'submit.html',{'form':form} )
def complete(request):
    return render(request,'complete.html')

def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST, request.FILES)
        if form.is_valid():
            if(len(request.FILES)!=0):
                todo = form.save(commit=False)
                todo.updated_at = timezone.datetime.now()
                todo.imgur = request.POST['imgur_url']
                print(todo.imgur)
                todo.save()
                return render(request,'complete.html')
            else:
                form2 = form
                return render(request,'submit.html', {'form':form})
    else:
        form = TodoForm()
    return render(request,'submit.html', {'form':form})