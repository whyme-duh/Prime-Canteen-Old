from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def wishlist(request):
	return render(request, 'canteenWishlist/wishlist.html')