from django.shortcuts import render
from .forms import MyForm


# Create your views here.


def form(request):
    if request.method == 'POST':
        data = MyForm(request.POST)
        if data.is_valid():
            name = data.cleaned_data['name']
            age = data.cleaned_data['age']
            gender = data.cleaned_data['gender']
            birthday = data.cleaned_data['birthday']
            address = data.cleaned_data['address']
            city = data.cleaned_data['city']
            state = data.cleaned_data['state']
            country = data.cleaned_data['country']
            phone = data.cleaned_data['phone']
            print(name, age, gender, birthday, address)
            print(city, state, country, phone)
            return render(request, 'form/success.html', {'name': name})
            # return HttpResponseRedirect('form/success.html')
    else:
        data = MyForm()
    return render(request, 'form/form.html', {'form': data})
