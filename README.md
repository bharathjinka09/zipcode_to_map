# Installation
pip install zipcode-to-map

# zipcode_to_map
Provide a Country code and postal code. It will generate a map in a html file based on these details. Used pgeocode and folium packages.

# Requirement Packages

## folium
pip install folium

## pgeocode
pip install pgeocode

# Example Usage

# Import the class

from zipcode_to_map.zipcode_to_map import ZipcodeToMap

# Instantiate the object

result_map = ZipcodeToMap()

# Provides the map as result
# Here 'in' is Country Code as India.
# '515411' is Pincode of a city.

result_map.zipcode_to_map('in','515411')

# Example to copy

from zipcode_to_map.zipcode_to_map import ZipcodeToMap

result_map = ZipcodeToMap()

result_map.zipcode_to_map('in','515411')
