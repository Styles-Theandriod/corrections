from django.shortcuts import render 

def index(request):
    return render(request, 'index.html')

def check_age(request):
    if request.method == 'POST':
        # Get the age from the form
        age = int(request, POST.get('age', 0))
        return render(request, 'check_age.html', {'age': age})
    return render(request, 'check_age.html')

def loop(request):
    data = 'Django is the best '
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    context = {
        'data': data,
        'number_list': number_list
    }
    return render(request, 'loop.html', context)