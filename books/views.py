from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

def home(request):
    register_url = reverse('register')
    return HttpResponse(f"""
                        <h1>Hello Bookworm!</h1>
                        <p>Welcome to your book tracking app.</p>
                        <p><a href="{register_url}">Create an Account</a></p>
                        """)