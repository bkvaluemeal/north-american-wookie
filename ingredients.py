class MasaHarina:
	nutrition = {
		'calories': 365,
		'carbs': 76.29,
		'fiber': 6.7,
		'protein': 9.3,
		'total_fat': 3.86,
		'saturated_fat': 0.5,
		'monounsaturated_fat': 0,
		'polyunsaturated_fat': 0,
		'omega_3': 0.052,
		'omega_6': 1.672,
		'cholesterol': 0,
		'vitamin a': 1000,
		'vitamin c': 0,
		'vitamin d': 0,
		'vitamin e': 0,
		'vitamin k': 0.3,
		'thiamin': 1.4,
		'riboflavin': 0.097,
		'niacin': 0,
		'vitamin b6': 0.475,
		'folic acid': 29,
		'vitamin b12': 0,
		'biotin': 0,
		'pantothenic acid': 0.7,
		'calcium': 0.141,
		'iron': 7.2,
		'phosphorus': 0.223,
		'iodine': 0,
		'magnesium': 110,
		'zinc': 1.8,
		'selenium': 14,
		'copper': 0.18,
		'manganese': 0.5,
		'chromium': 0,
		'molybdenum': 0,
		'chloride': 0,
		'potassium': 0.298,
		'boron': 0,
		'nickel': 0,
		'silicon': 0,
		'tin': 0,
		'vanadium': 0,
		'lycopene': 0,
		'choline': 8.6
	}
	info = {
		'name': 'Masa Harina',
		'unit': 'g',
		'size': 2000,
		'price': 2.88,
		'source': 'walmart',
		'link': 'http://www.walmart.com/ip/10291185'
	}

	def __init__(self, x):
		self.x = x
		for key in self.nutrition:
			self.nutrition[key] *= x/100

	def getNutrition(self):
		return self.nutrition

	def getInfo(self):
		return self.info

	def getPrice(self):
		return (self.x / self.info['size']) * self.info['price']

	def getName(self):
		return self.info['name']

	def getUnit(self):
		return self.info['unit']
