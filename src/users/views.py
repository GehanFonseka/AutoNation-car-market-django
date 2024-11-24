from http.client import HTTPResponse
from django.shortcuts import render

def login_view(request):
    return HTTPResponse("Login View :)")
