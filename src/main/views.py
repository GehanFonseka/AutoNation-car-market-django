from django.http import HttpResponse
from django.shortcuts import render
 
def main_view(request):
    return render(request, "views/main.html", {"name": "AutoMax"})
