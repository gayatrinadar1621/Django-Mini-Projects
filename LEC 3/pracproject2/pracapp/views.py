from django.shortcuts import render

# Create your views here.

def home(request):
	if request.POST.get('hp'):
		return render(request,'home.html',{'picture':'HP'})

	elif request.POST.get('twi'):
		return render(request,'home.html',{'picture':'TWI'})

	elif request.POST.get('maze'):
		return render(request,'home.html',{'picture':'MAZE'})

	else:
		return render(request,'home.html')

	
