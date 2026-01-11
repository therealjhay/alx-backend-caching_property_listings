import logging
from django.core.cache import cache
from django_redis import get_redis_connection
from .models import Property

# Set up a logger
logger = logging.getLogger(__name__)

def get_all_properties():
    # ... (Keep your existing function exactly as it is) ...
    properties = cache.get('all_properties')
    if properties is None:
        properties = Property.objects.all()
        cache.set('all_properties', properties, 3600)
    return properties

def get_redis_cache_metrics():
    """
    Connects to Redis to retrieve hit/miss statistics.
    """
    try:
        # Get the raw Redis connection
        redis_conn = get_redis_connection("default")
        
        # Get Redis statistics
        info = redis_conn.info()
        
        # Extract specific keyspace stats
        hits = info.get('keyspace_hits', 0)
        misses = info.get('keyspace_misses', 0)
        total_requests = hits + misses
        
        # Calculate ratio (avoid division by zero)
        if total_requests > 0:
            hit_ratio = hits / total_requests
        else:
            hit_ratio = 0

        metrics = {
            'hits': hits,
            'misses': misses,
            'hit_ratio': hit_ratio
        }

        # Log the metrics
        logger.info(f"Redis Cache Metrics: {metrics}")

        return metrics

    except Exception as e:
        logger.error(f"Failed to retrieve Redis metrics: {e}")
        return {'error': str(e)}