import pgeocode
import folium


'''
Provide a Country code and postal code.
It will generate a map in a html file based on these details.
Used pgeocode and folium packages.
'''
class ZipcodeToMap:

	def zipcode_to_map(self, country_code, postal_code):
		country_code = pgeocode.Nominatim(country_code)

		zip_code = country_code.query_postal_code(postal_code)

		postal_code = zip_code['postal_code']


		m = folium.Map(location=[zip_code['latitude'], zip_code['longitude']], zoom_start=12,
		                   detect_retina=True, control_scale=True)

		m.save(f'{postal_code}-map.html')
		print(f'Map generated for {postal_code} postal code')
		
		return f'Map generated for {postal_code} postal code'
