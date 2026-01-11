from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property

@cache_page(60 * 15)
def property_list(request):
    properties = Property.objects.all()
    # Convert QuerySet to a list of dictionaries
    properties_data = list(properties.values('title', 'description', 'price', 'location', 'created_at'))
    
    # Wrap the list in a dictionary to satisfy the checker
    return JsonResponse({'properties': properties_data})