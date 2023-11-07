from django.shortcuts import render

# Create your views here.

def home(request):
	if request.GET.get('r'):
		return render(request, 'home.html', {'color':'#ff4d4d'})
	elif request.GET.get('y'):
		return render(request, 'home.html', {'color':'#ffff4d'})
	elif request.GET.get('g'):
		return render(request, 'home.html', {'color':'#47d147'})
	else:
		return render(request, 'home.html')
