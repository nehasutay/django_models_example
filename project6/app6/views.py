from django.shortcuts import render
from app6.models import emp 

# Create your views here.
def form(request):
    return render(request,"form.html")

# def save(request):
# 	p=emp(name=request.POST.get('name'), addr=request.POST.get('addr'))
# 	p.save()

def show(request):
	data={
	'name'=request.POST.get('name'),
	'addr'=request.POST.get('addr')
	}
	return render(request,"show.html",data)

def create(request):
	emp.objects.create(name="abc", addr="ngp")
	return render(request,"create.html")




	



		    
