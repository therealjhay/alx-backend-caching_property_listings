from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property

# Cache the response for 15 minutes (60 seconds * 15)
@cache_page(60 * 15)
def property_list(request):
    # Get all properties from the database
    properties = Property.objects.all()
    
    # Convert query set to a list of dictionaries so we can return JSON
    # (If you were using templates, you would just pass 'properties' in the context)
    properties_list = list(properties.values('title', 'price', 'location', 'description'))
    
    return JsonResponse(properties_list, safe=False)