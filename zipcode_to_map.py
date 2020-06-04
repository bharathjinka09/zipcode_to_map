import pgeocode
import folium


'''
Provide a Country code and postal code.
It will generate a map in a html file based on these details.
Used pgeocode and folium packages.
'''

def zipcode_to_map(country_code, postal_code):
	country_code = pgeocode.Nominatim(country_code)

	zip_code = country_code.query_postal_code(postal_code)

	postal_code = zip_code['postal_code']

	# print(postal_code)
	# print(zip_code)
	# print(zip_code['latitude'])
	# print(zip_code['longitude'])

	multiple_zip_codes = country_code.query_postal_code(["560034", "560083"])

	# print(multiple_zip_codes)

	# print(multiple_zip_codes['latitude'])


	m = folium.Map(location=[zip_code['latitude'], zip_code['longitude']], zoom_start=9,
	                   detect_retina=True, control_scale=False)

	m.save(f'{postal_code}-map.html')

zipcode_to_map('in','515411')