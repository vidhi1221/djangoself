from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def hour_display(request):
    d=datetime.datetime.now()
    h=int(d.strftime('%H'))
    msg="GOOD"
    if h<12:
        msg+=" MORNING"
        return render(request,'testapp/morning.html',{'m':msg,'date':d})

    elif h<16:
        msg+=" AFTERNOON"
        return render(request,'testapp/afternoon.html',{'m':msg,'date':d})

    elif h<21:
        msg+=" EVENING"
        return render(request,'testapp/evening.html',{'m':msg,'date':d})

    else:
        msg+=" NIGHT"
        return render(request,'testapp/night.html',{'m':msg,'date':d})

    
