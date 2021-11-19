from os import strerror
from django.shortcuts import redirect, render

from new.models import Token

# Create your views here.



def one(request):
    a=Token.objects.all()
    for i in a:
        b=i.id
    if b<10:
        c='ITEMSUB00'+str(b)
        
    elif 10<=b<100:
        c='ITEMSUB0'+str(b)
    elif 100<=b<1000:
        c='ITEMSUB'+str(b)
    return render(request,'new/second.html',{'a':c})





def home(request):
    if request.method=='POST':
        a=Token.objects.create()
        
        return redirect('one')

    return render(request,'new/first.html')
