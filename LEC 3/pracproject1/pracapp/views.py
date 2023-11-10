from django.shortcuts import render

# Create your views here.

def home(request):
	if request.GET.get('n1') and request.GET.get('n2'):
		n1 = int(request.GET.get('n1'))
		n2 = int(request.GET.get('n2'))

		msg = "Addition of " + str(n1) + " and " + str(n2) + " is " + str(n1+n2)
		return render(request, 'home.html', {'msg':msg})


	if request.GET.get('sqr'):
		n3 = float(request.GET.get('n3'))
	
		ans = "Square of " + str(n3) +  " is " + str(n3*n3)
		return render(request, 'home.html', {'ans':ans})

	elif request.GET.get('cube'):
		n3 = float(request.GET.get('n3'))
	
		ans = "Cube of " + str(n3) +  " is " + str(n3*n3*n3)
		return render(request, 'home.html', {'ans':ans})

	else:
		return render(request, 'home.html')


