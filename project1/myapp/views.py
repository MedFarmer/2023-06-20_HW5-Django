from django.shortcuts import render, redirect
from .models import Hotel

def index(request):
    hotels_objects = Hotel.objects.all()
           
    if request.method == 'POST' and (request.POST['hotel_name'] != ''):
        hotel_name = request.POST['hotel_name']
        hotel_address = request.POST['hotel_address']
        hotel_description = request.POST['hotel_description']
        Hotel.objects.create(hotel_name=hotel_name, hotel_address=hotel_address, hotel_description=hotel_description)    
        return redirect(index)
    else:
        return render(request, 'index.html', {'hotels':hotels_objects})
    
def about(request):
    hotels_addresses = []
    k = 0
    hotels_objects = Hotel.objects.all()
    for i in hotels_objects:
        k += 1
        hotels_addresses.append(i.hotel_address)
    
    return render(request, 'about.html', {'hotel_num':k, 'hotels_addresses':hotels_addresses})

def contacts(request):
    return render(request, 'contacts.html')
