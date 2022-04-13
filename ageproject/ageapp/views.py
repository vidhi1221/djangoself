from django.shortcuts import render
from datetime import date

# Create your views here.

def age_res(birthdate):
    return render(birthdate, 'age.html')

def search(birthdate,request):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        if age > 18 and age < 60 :
            age += "You are elligible"
        elif age < 18 or age > 60 :
            age += "You are not elligible"
    return render(birthdate,'testapp/age.html') 