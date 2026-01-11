from django.shortcuts import render
from django.http import JsonResponse
from .utils import get_all_properties  # Import your new function

# Remove @cache_page decorator
def property_list(request):
    # Call the utility function to get data (cached or fresh)
    properties = get_all_properties()
    
    # Convert QuerySet to list of dicts for JSON response
    properties_data = list(properties.values('title', 'description', 'price', 'location', 'created_at'))
    
    return JsonResponse({'properties': properties_data})