from django.shortcuts import render
from app2.models import cust

# Create your views here.

def show(request):
	data={
	'name':request.POST.get('name'),
	'addr':request.POST.get('addr')
	}
	return render(request,"show.html",data)

def create(request):
	cust.objects.create(name=request.POST.get('name'), addr=request.POST.get('addr'))
	return render(request,"create.html")

def display(request):
	a=cust.objects.all()
	data={'obj':a}
	return render(request,"display.html",data)

def search(request,id):
	print(id)
	a=cust.objects.get(pk=id)
	data={'obj':a}
	return render(request,"search.html",data)

def form(request):
	return render(request,"form.html")



# def displayone(request):
# 	a=cust.objects.get()





