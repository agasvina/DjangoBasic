from django.db import models
from django.conf import settings

class Todo(models.Model):
	# TODO Category:
	WORK = 'W'
	LEISURE = 'L'
	MISC = 'O'
	CATEGORIES_CHOICES = (
		(WORK, 'Work'),
		(LEISURE, 'Leisure'),
		(MISC, 'Misc'),
	)

	#Foreign key connect different model together
	#Remember, here the admin  and todo table are located 
	# within the same DB
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	todo = models.TextField()
	category = models.CharField(
		max_length = 2,
		choices = CATEGORIES_CHOICES,
		default = MISC,
	)
	completed = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.todo

	class Meta:
		db_table = 'todo'
