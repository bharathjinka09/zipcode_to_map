# zipcode_to_map
Provide a Country code and postal code. It will generate a map in a html file based on these details. Used pgeocode and folium packages.

# Example Usage

# Import the class

from zipcode_to_map.zipcode_to_map import ZipcodeToMap

# Instantiate the object

result_map = ZipcodeToMap()

# Provides the map as result
# Here 'in' is Country Code as India.
# '515411' is Pincode of a city.

result_map.zipcode_to_map('in','515411')
