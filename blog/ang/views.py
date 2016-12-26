from django.shorcuts import render

def get_angular_template(request, path=None):
	return render(request, "ang/index.html", {})