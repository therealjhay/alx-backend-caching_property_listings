from django.core.cache import cache
from .models import Property

def get_all_properties():
    # 1. Try to get the data from Redis
    properties = cache.get('all_properties')

    # 2. If it is NOT in Redis (returns None), fetch from DB and save it
    if properties is None:
        properties = Property.objects.all()
        
        # 3. Save to Redis for 1 hour (3600 seconds)
        cache.set('all_properties', properties, 3600)

    # 4. Return the data (either from cache or DB)
    return properties