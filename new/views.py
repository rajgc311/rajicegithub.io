from django.shortcuts import render, HttpResponse
from new.models import Booking


# Create your views here.
def index(request):
	return render(request, 'index.html')

def varieties(request):
	return render (request,'varieties.html')

def strawberry(request):
	return render(request,'strawberry.html')

def butterscotch(request):
	return render(request,'butterscotch.html')

def gelato(request):
	return render(request,'Gelato.html')

def thankyou(request):
	return render(request,'thankyou.html')

def chocolate(request):
	return render(request,'chocolate.html')

def forbooking(request):
	if request.method == "POST":
		name = request.POST['name']
		address = request.POST['address']
		types = request.POST['types']
		quantity = request.POST['quantity']
		location = request.POST['location']
		description = request.POST['description']
		booking = Booking(name=name, address=address, types=types, quantity=quantity, location=location, description=description)
		booking.save()
		


	return render(request,'forbooking.html')
    
