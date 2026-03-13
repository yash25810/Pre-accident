

# Importing requests to make HTTP calls to LOCATION_API
import requests

def get_nearest_hospital(crash_lat, crash_lon, radius_km=10):
    """
    Given the latitude and longitude of a crash, this function dynamically finds the nearest hospital
    using the LOCATION_API (external service) instead of OpenStreetMap/overpy.
    Args:
        crash_lat (float): Latitude of the crash location
        crash_lon (float): Longitude of the crash location
        radius_km (float): Search radius in kilometers (default: 10km)
    Returns:
        tuple: (nearest hospital name, distance in kilometers)
    """
    # LOCATION_API endpoint (should be set in environment/config)
    # Example: 'https://api.locationiq.com/v1/nearby.php?key=YOUR_API_KEY&lat={lat}&lon={lon}&tag=hospital&radius={radius}'
    import os
    LOCATION_API_URL = os.getenv('LOCATION_API_URL')  # Should be set in .env or config
    LOCATION_API_KEY = os.getenv('LOCATION_API_KEY')  # Should be set in .env or config

    if not LOCATION_API_URL or not LOCATION_API_KEY:
        # If API URL or KEY is not set, return error
        print("LOCATION_API_URL or LOCATION_API_KEY not set in environment.")
        return None, 0

    # Build the request parameters for the API
    params = {
        'key': LOCATION_API_KEY,
        'lat': crash_lat,
        'lon': crash_lon,
        'tag': 'hospital',
        'radius': int(radius_km * 1000),  # Convert km to meters
        'format': 'json'
    }

    try:
        # Make the API request
        response = requests.get(LOCATION_API_URL, params=params, timeout=10)
        response.raise_for_status()  # Raise error for bad status
        hospitals = response.json()
    except Exception as e:
        # If API fails, return None and 0 distance
        print(f"Error querying LOCATION_API: {e}")
        return None, 0

    # If the API returns a list of hospitals, find the nearest one
    if isinstance(hospitals, list) and hospitals:
        # Assume the first hospital is the nearest (API should sort by distance)
        nearest = hospitals[0]
        # Extract hospital name and distance (API response structure may vary)
        hospital_name = nearest.get('name', 'Unknown Hospital')
        # Some APIs provide distance in meters, convert to km
        distance_m = nearest.get('distance', 0)
        distance_km = float(distance_m) / 1000 if distance_m else 0
        return hospital_name, distance_km
    else:
        # No hospitals found in the area
        return "No hospital found nearby", 0


# Note:
# - This utility function now uses LOCATION_API for real-time hospital lookup.
# - LOCATION_API_URL and LOCATION_API_KEY must be set in the environment or .env file.
# - The function is dynamic and location-independent.
# - The search radius can be adjusted as needed.
# - All logic and variables are explained above for clarity and maintainability.
# - If the API response structure is different, adjust the parsing logic accordingly.

