class Wishlist():
	def __init__(self, request):
		
		self.session = request.session
		wishlist = self.session.get('sessionKey')
		if 'sessionKey' not in request.session:
			wishlist = self.session['sessionKey'] = {}
		self.wishlist = wishlist

