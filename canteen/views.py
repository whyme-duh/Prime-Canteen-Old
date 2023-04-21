from django.shortcuts import get_object_or_404, render

from .models import Food

context ={
	
	'foods' : Food.objects.all()
}


def home(request):
	return render(request,context = context, template_name="canteen/home.html")

def detail(request, slug):
	food = get_object_or_404(Food, slug= slug, still_left = True)
	return render(request, 'canteen/food-detail.html' ,{'food' : food})


