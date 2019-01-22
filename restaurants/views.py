from django.shortcuts import render
# from django.http import HttpResponse


# Create your views here.
context ={
	"msg": "Hello World!"
}
def home(request):
	return render(request, 'taskTwo.html' , context)
