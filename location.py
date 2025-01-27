import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium

# API Key for OpenCageGeocode
Key = "6d6f969fd9024ac8afde957f0c86a5ba"

# Input phone number with country code
number = input("Enter phone number with country code: ")

# Parse phone number
check_number = phonenumbers.parse(number)

# Get location description for the number
number_location = geocoder.description_for_number(check_number, "en")
print(f"Location: {number_location}")

# Get carrier name for the number
service_provider = carrier.name_for_number(check_number, "en")
print(f"Carrier: {service_provider}")

# Initialize OpenCageGeocode with API Key
geocoder = OpenCageGeocode(Key)

# Geocode the location to get latitude and longitude
query = str(number_location)
results = geocoder.geocode(query)

# Extract latitude and longitude from results
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(f"Latitude: {lat}, Longitude: {lng}")

# Create a map centered at the location
map_location = folium.Map(location=[lat, lng], zoom_start=9)

# Add a marker for the location
folium.Marker([lat, lng], popup=number_location).add_to(map_location)

# Save the map as an HTML file
map_location.save("mylocation.html")
