from django.shortcuts import render 

def menu(request):
    return render(request, 'menu.html')

# Create your views here.

from rest_framework.views import APIView
from django.shortcuts import render

class MenuHTMLView(APIView):
    def get(self, request):
        return render(request, 'menu.html')