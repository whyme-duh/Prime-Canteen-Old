from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class Profile(models.Model):
	CSIT= "CSIT"
	BIM = "BIM"
	BCA = "BCA"
	BBA = "BBA"
	BBS = "BBS"


	FACULTIES = [
		(CSIT, "CSIT"),
		(CSIT, "CSIT"),
		(BIM , "BIM"),
		(BCA , "BCA"),
		(BBA , "BBA"),
		(BBS , "BBS"),
	]

	name = models.OneToOneField(User, on_delete=models.CASCADE)
	faculty = models.CharField(max_length = 50, choices = FACULTIES ,)

	def __str__(self):
		return self.name

	