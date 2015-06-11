class MasaHarina:
	info = {
		'name': 'Masa Harina',
		'unit': 'g',
		'size': 2000,
		'price': 2.88,
		'source': 'walmart',
		'link': 'http://www.walmart.com/ip/10291185'
	}

	def __init__(self, x):
		self.nutrition = {
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
			'choline': 8.6,
			'sodium': 0
		}
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

class SoyFlour:
	info = {
		'name': 'Soy Flour',
		'unit': 'g',
		'size': 22680,
		'price': 56.99,
		'source': 'amazon',
		'link': 'http://amzn.com/B00993C02U'
	}

	def __init__(self, x):
		self.nutrition = {
			'calories': 300,
			'carbs': 35,
			'fiber': 18,
			'protein': 51,
			'total_fat': 2,
			'saturated_fat': 0.5,
			'monounsaturated_fat': 0.2,
			'polyunsaturated_fat': 0.6,
			'omega_3': 0.066,
			'omega_6': 0.493,
			'cholesterol': 0,
			'vitamin a': 40,
			'vitamin c': 0,
			'vitamin d': 0,
			'vitamin e': 0.2,
			'vitamin k': 4.3,
			'thiamin': 0.7,
			'riboflavin': 0.3,
			'niacin': 2.7,
			'vitamin b6': 0.6,
			'folic acid': 320,
			'vitamin b12': 0,
			'biotin': 0,
			'pantothenic acid': 2.1,
			'calcium': 0.3,
			'iron': 5,
			'phosphorus': 0.708,
			'iodine': 0,
			'magnesium': 304,
			'zinc': 2.6,
			'selenium': 1.8,
			'copper': 4.3,
			'manganese': 3.2,
			'chromium': 0,
			'molybdenum': 0,
			'chloride': 0,
			'potassium': 2.5,
			'boron': 0,
			'nickel': 0,
			'silicon': 0,
			'tin': 0,
			'vanadium': 0,
			'lycopene': 0,
			'choline': 11.9,
			'sodium': 0
		}
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

class OatFlour:
	info = {
		'name': 'Oat Flour',
		'unit': 'g',
		'size': 22680,
		'price': 57.99,
		'source': 'amazon',
		'link': 'http://amzn.com/B007KVA5CU'
	}

	def __init__(self, x):
		self.nutrition = {
			'calories': 398,
			'carbs': 65,
			'fiber': 12.5,
			'protein': 16,
			'total_fat': 7.2,
			'saturated_fat': 1.5,
			'monounsaturated_fat': 2.9,
			'polyunsaturated_fat': 3.3,
			'omega_3': 0.145,
			'omega_6': 3.185,
			'cholesterol': 0,
			'vitamin a': 0,
			'vitamin c': 0,
			'vitamin d': 0,
			'vitamin e': 1,
			'vitamin k': 3.2,
			'thiamin': 0.7,
			'riboflavin': 0.1,
			'niacin': 1.5,
			'vitamin b6': 0.1,
			'folic acid': 32,
			'vitamin b12': 0,
			'biotin': 0,
			'pantothenic acid': 0.2,
			'calcium': 0.055,
			'iron': 2.5,
			'phosphorus': 0.453,
			'iodine': 0,
			'magnesium': 144,
			'zinc': 3.2,
			'selenium': 34,
			'copper': 0.4,
			'manganese': 4,
			'chromium': 0,
			'molybdenum': 200,
			'chloride': 0,
			'potassium': 0.371,
			'boron': 0,
			'nickel': 0,
			'silicon': 0,
			'tin': 0,
			'vanadium': 0,
			'lycopene': 0,
			'choline': 29.9,
			'sodium': 0
		}
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

class Dextrose:
	info = {
		'name': 'Dextrose',
		'unit': 'g',
		'size': 22680,
		'price': 53.99,
		'source': 'amazon',
		'link': 'http://amzn.com/B0097FJK46'
	}

	def __init__(self, x):
		self.nutrition = {
			'calories': 375,
			'carbs': 100,
			'fiber': 0,
			'protein': 0,
			'total_fat': 0,
			'saturated_fat': 0,
			'monounsaturated_fat': 0,
			'polyunsaturated_fat': 0,
			'omega_3': 0,
			'omega_6': 0,
			'cholesterol': 0,
			'vitamin a': 0,
			'vitamin c': 0,
			'vitamin d': 0,
			'vitamin e': 0,
			'vitamin k': 0,
			'thiamin': 0,
			'riboflavin': 0,
			'niacin': 0,
			'vitamin b6': 0,
			'folic acid': 0,
			'vitamin b12': 0,
			'biotin': 0,
			'pantothenic acid': 0,
			'calcium': 0,
			'iron': 0,
			'phosphorus': 0,
			'iodine': 0,
			'magnesium': 0,
			'zinc': 0,
			'selenium': 0,
			'copper': 0,
			'manganese': 0,
			'chromium': 0,
			'molybdenum': 0,
			'chloride': 0,
			'potassium': 0,
			'boron': 0,
			'nickel': 0,
			'silicon': 0,
			'tin': 0,
			'vanadium': 0,
			'lycopene': 0,
			'choline': 0,
			'sodium': 0
		}
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

class Maltodextrin:
	info = {
		'name': 'Maltodextrin',
		'unit': 'g',
		'size': 22680,
		'price': 63.99,
		'source': 'amazon',
		'link': 'http://amzn.com/B0098QJPO4'
	}

	def __init__(self, x):
		self.nutrition = {
			'calories': 380,
			'carbs': 94,
			'fiber': 0,
			'protein': 0,
			'total_fat': 0,
			'saturated_fat': 0,
			'monounsaturated_fat': 0,
			'polyunsaturated_fat': 0,
			'omega_3': 0,
			'omega_6': 0,
			'cholesterol': 0,
			'vitamin a': 0,
			'vitamin c': 0,
			'vitamin d': 0,
			'vitamin e': 0,
			'vitamin k': 0,
			'thiamin': 0,
			'riboflavin': 0,
			'niacin': 0,
			'vitamin b6': 0,
			'folic acid': 0,
			'vitamin b12': 0,
			'biotin': 0,
			'pantothenic acid': 0,
			'calcium': 0,
			'iron': 0,
			'phosphorus': 0,
			'iodine': 0,
			'magnesium': 0,
			'zinc': 0,
			'selenium': 0,
			'copper': 0,
			'manganese': 0,
			'chromium': 0,
			'molybdenum': 0,
			'chloride': 0,
			'potassium': 0,
			'boron': 0,
			'nickel': 0,
			'silicon': 0,
			'tin': 0,
			'vanadium': 0,
			'lycopene': 0,
			'choline': 0,
			'sodium': 0
		}
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

class PotatoStarch:
	info = {
		'name': 'Potato Starch',
		'unit': 'g',
		'size': 22680,
		'price': 70.99,
		'source': 'amazon',
		'link': 'http://amzn.com/B0098QBMIG'
	}

	def __init__(self, x):
		self.nutrition = {
			'calories': 331,
			'carbs': 82.645,
			'fiber': 0,
			'protein': 0,
			'total_fat': 0,
			'saturated_fat': 0,
			'monounsaturated_fat': 0,
			'polyunsaturated_fat': 0,
			'omega_3': 0,
			'omega_6': 0,
			'cholesterol': 0,
			'vitamin a': 0,
			'vitamin c': 0,
			'vitamin d': 0,
			'vitamin e': 0,
			'vitamin k': 0,
			'thiamin': 0,
			'riboflavin': 0,
			'niacin': 0,
			'vitamin b6': 0,
			'folic acid': 0,
			'vitamin b12': 0,
			'biotin': 0,
			'pantothenic acid': 0,
			'calcium': 0,
			'iron': 0,
			'phosphorus': 0,
			'iodine': 0,
			'magnesium': 0,
			'zinc': 0,
			'selenium': 0,
			'copper': 0,
			'manganese': 0,
			'chromium': 0,
			'molybdenum': 0,
			'chloride': 0,
			'potassium': 0,
			'boron': 0,
			'nickel': 0,
			'silicon': 0,
			'tin': 0,
			'vanadium': 0,
			'lycopene': 0,
			'choline': 0,
			'sodium': 0
		}
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

class CornStarch:
	info = {
		'name': 'Corn Starch',
		'unit': 'g',
		'size': 22680,
		'price': 53.99,
		'source': 'amazon',
		'link': 'http://amzn.com/B0098Q1LSM'
	}

	def __init__(self, x):
		self.nutrition = {
			'calories': 381,
			'carbs': 91.3,
			'fiber': 0.9,
			'protein': 0.3,
			'total_fat': 0.1,
			'saturated_fat': 0,
			'monounsaturated_fat': 0,
			'polyunsaturated_fat': 0,
			'omega_3': 0,
			'omega_6': 25,
			'cholesterol': 0,
			'vitamin a': 0,
			'vitamin c': 0,
			'vitamin d': 0,
			'vitamin e': 0,
			'vitamin k': 0,
			'thiamin': 0,
			'riboflavin': 0,
			'niacin': 0,
			'vitamin b6': 0,
			'folic acid': 0,
			'vitamin b12': 0,
			'biotin': 0,
			'pantothenic acid': 0,
			'calcium': 2,
			'iron': 0.5,
			'phosphorus': 13,
			'iodine': 0,
			'magnesium': 3,
			'zinc': 0.1,
			'selenium': 2.8,
			'copper': 0.1,
			'manganese': 0.1,
			'chromium': 0,
			'molybdenum': 0,
			'chloride': 0,
			'potassium': 3,
			'boron': 0,
			'nickel': 0,
			'silicon': 0,
			'tin': 0,
			'vanadium': 0,
			'lycopene': 0,
			'choline': 0.4,
			'sodium': 9
		}
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

class WhiteRiceFlour:
	info = {
		'name': 'White Rice Flour',
		'unit': 'g',
		'size': 22680,
		'price': 60.99,
		'source': 'amazon',
		'link': 'http://amzn.com/B0097EY2QS'
	}

	def __init__(self, x):
		self.nutrition = {
			'calories': 366,
			'carbs': 80.1,
			'fiber': 2.4,
			'protein': 5.9,
			'total_fat': 1.4,
			'saturated_fat': 0.4,
			'monounsaturated_fat': 0.4,
			'polyunsaturated_fat': 0.4,
			'omega_3': 67,
			'omega_6': 313,
			'cholesterol': 0,
			'vitamin a': 0,
			'vitamin c': 0,
			'vitamin d': 0,
			'vitamin e': 0.15,
			'vitamin k': 0,
			'thiamin': 0.1,
			'riboflavin': 0,
			'niacin': 2.6,
			'vitamin b6': 0.4,
			'folic acid': 4,
			'vitamin b12': 0,
			'biotin': 0,
			'pantothenic acid': 0.8,
			'calcium': 10,
			'iron': 0.4,
			'phosphorus': 98,
			'iodine': 0,
			'magnesium': 35,
			'zinc': 0.8,
			'selenium': 15.1,
			'copper': 0.1,
			'manganese': 1.2,
			'chromium': 0,
			'molybdenum': 0,
			'chloride': 0,
			'potassium': 76,
			'boron': 0,
			'nickel': 0,
			'silicon': 0,
			'tin': 0,
			'vanadium': 0,
			'lycopene': 0,
			'choline': 5.8,
			'sodium': 0
		}
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

class BrownRiceFlour:
	info = {
		'name': 'Brown Rice Flour',
		'unit': 'g',
		'size': 22680,
		'price': 66.99,
		'source': 'amazon',
		'link': 'http://amzn.com/B0098QDMCA'
	}

	def __init__(self, x):
		self.nutrition = {
			'calories': 363,
			'carbs': 76.5,
			'fiber': 4.6,
			'protein': 7.2,
			'total_fat': 2.8,
			'saturated_fat': 0.6,
			'monounsaturated_fat': 1,
			'polyunsaturated_fat': 1,
			'omega_3': 42,
			'omega_6': 954,
			'cholesterol': 0,
			'vitamin a': 0,
			'vitamin c': 0,
			'vitamin d': 0,
			'vitamin e': 1.8,
			'vitamin k': 0,
			'thiamin': 0.4,
			'riboflavin': 0.1,
			'niacin': 6.3,
			'vitamin b6': 0.7,
			'folic acid': 16,
			'vitamin b12': 0,
			'biotin': 0,
			'pantothenic acid': 1.6,
			'calcium': 11,
			'iron': 2,
			'phosphorus': 337,
			'iodine': 0,
			'magnesium': 112,
			'zinc': 2.5,
			'selenium': 0,
			'copper': 0.2,
			'manganese': 4,
			'chromium': 0,
			'molybdenum': 0,
			'chloride': 0,
			'potassium': 289,
			'boron': 0,
			'nickel': 0,
			'silicon': 0,
			'tin': 0,
			'vanadium': 0,
			'lycopene': 0,
			'choline': 0,
			'sodium': 8
		}
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

class BarleyFlour:
	info = {
		'name': 'Barley Flour',
		'unit': 'g',
		'size': 22680,
		'price': 43.99,
		'source': 'amazon',
		'link': 'http://amzn.com/B00993BW7Y'
	}

	def __init__(self, x):
		self.nutrition = {
			'calories': 345,
			'carbs': 74.5,
			'fiber': 10.1,
			'protein': 10.5,
			'total_fat': 1.6,
			'saturated_fat': 0.3,
			'monounsaturated_fat': 0.2,
			'polyunsaturated_fat': 0.8,
			'omega_3': 77,
			'omega_6': 695,
			'cholesterol': 0,
			'vitamin a': 0,
			'vitamin c': 0,
			'vitamin d': 0,
			'vitamin e': 0.9,
			'vitamin k': 2.2,
			'thiamin': 0.4,
			'riboflavin': 0.1,
			'niacin': 6.3,
			'vitamin b6': 0.4,
			'folic acid': 8,
			'vitamin b12': 0,
			'biotin': 0,
			'pantothenic acid': 0.1,
			'calcium': 32,
			'iron': 2.7,
			'phosphorus': 296,
			'iodine': 0,
			'magnesium': 96,
			'zinc': 2,
			'selenium': 37.7,
			'copper': 0.23,
			'manganese': 1,
			'chromium': 0,
			'molybdenum': 0,
			'chloride': 0,
			'potassium': 309,
			'boron': 0,
			'nickel': 0,
			'silicon': 0,
			'tin': 0,
			'vanadium': 0,
			'lycopene': 0,
			'choline': 37.8,
			'sodium': 4
		}
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
