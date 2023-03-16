from django.shortcuts import render

from item.models import Category,Item

from .forms import SingUpForm

def index(request):
    items =Item.objects.filter(is_sold=False)[0:6]
    categories=Category.objects.all()

    return render(request,'core/index.html' ,
                  {'categories': categories,
                   'items': items
                   })

def contact(request):
    return render(request,'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SingUpForm(request.POST)

        if form.is_valid():
            form.save()

            return render(request,'core/contact.html')
    form= SingUpForm()
    return render(request, 'core/signup.html', {
        'form':form
    })
