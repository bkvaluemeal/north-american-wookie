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

	def getX(self):
		return self.x

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

	def getX(self):
		return self.x

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

	def getX(self):
		return self.x

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

	def getX(self):
		return self.x

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

	def getX(self):
		return self.x

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

	def getX(self):
		return self.x

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

	def getX(self):
		return self.x

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

	def getX(self):
		return self.x

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

	def getX(self):
		return self.x

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

	def getX(self):
		return self.x

class AllPurposeFlour:
	info = {
		'name': 'All Purpose Flour',
		'unit': 'g',
		'size': 22680,
		'price': 41.99,
		'source': 'amazon',
		'link': 'http://amzn.com/B0007NC134'
	}

	def __init__(self, x):
		self.nutrition = {
			'calories': 364,
			'carbs': 76.3,
			'fiber': 2.7,
			'protein': 10.3,
			'total_fat': 1,
			'saturated_fat': 0.2,
			'monounsaturated_fat': 0.1,
			'polyunsaturated_fat': 0.4,
			'omega_3': 22,
			'omega_6': 391,
			'cholesterol': 0,
			'vitamin a': 0,
			'vitamin c': 0,
			'vitamin d': 0,
			'vitamin e': 0.15,
			'vitamin k': 0.3,
			'thiamin': 0.8,
			'riboflavin': 0.5,
			'niacin': 5.9,
			'vitamin b6': 0,
			'folic acid': 183,
			'vitamin b12': 0,
			'biotin': 0,
			'pantothenic acid': 0.4,
			'calcium': 15,
			'iron': 4.6,
			'phosphorus': 108,
			'iodine': 0,
			'magnesium': 22,
			'zinc': 0.7,
			'selenium': 33.9,
			'copper': 0.1,
			'manganese': 0.7,
			'chromium': 0,
			'molybdenum': 0,
			'chloride': 0,
			'potassium': 107,
			'boron': 0,
			'nickel': 0,
			'silicon': 0,
			'tin': 0,
			'vanadium': 0,
			'lycopene': 0,
			'choline': 10.4,
			'sodium': 2
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

	def getX(self):
		return self.x

class WholeWheatFlour:
	info = {
		'name': 'Whole Wheat Flour',
		'unit': 'g',
		'size': 22680,
		'price': 41.99,
		'source': 'amazon',
		'link': 'http://amzn.com/B0096QV21U'
	}

	def __init__(self, x):
		self.nutrition = {
			'calories': 339,
			'carbs': 72.6,
			'fiber': 12.2,
			'protein': 13.7,
			'total_fat': 1.9,
			'saturated_fat': 0.3,
			'monounsaturated_fat': 0.2,
			'polyunsaturated_fat': 0.8,
			'omega_3': 38,
			'omega_6': 738,
			'cholesterol': 0,
			'vitamin a': 9,
			'vitamin c': 0,
			'vitamin d': 0,
			'vitamin e': 1.2,
			'vitamin k': 1.9,
			'thiamin': 0.4,
			'riboflavin': 0.2,
			'niacin': 6.4,
			'vitamin b6': 0.3,
			'folic acid': 44,
			'vitamin b12': 0,
			'biotin': 0,
			'pantothenic acid': 1,
			'calcium': 34,
			'iron': 3.9,
			'phosphorus': 346,
			'iodine': 0,
			'magnesium': 138,
			'zinc': 2.9,
			'selenium': 70.7,
			'copper': 0.4,
			'manganese': 3.8,
			'chromium': 0,
			'molybdenum': 0,
			'chloride': 0,
			'potassium': 405,
			'boron': 0,
			'nickel': 0,
			'silicon': 0,
			'tin': 0,
			'vanadium': 0,
			'lycopene': 0,
			'choline': 31.2,
			'sodium': 5
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

	def getX(self):
		return self.x

class YellowCornMeal:
	info = {
		'name': 'Yellow Corn Meal',
		'unit': 'g',
		'size': 22680,
		'price': 43.99,
		'source': 'amazon',
		'link': 'http://amzn.com/B0096Q5IO2'
	}

	def __init__(self, x):
		self.nutrition = {
			'calories': 362,
			'carbs': 76.9,
			'fiber': 7.3,
			'protein': 8.1,
			'total_fat': 3.6,
			'saturated_fat': 0.5,
			'monounsaturated_fat': 0.9,
			'polyunsaturated_fat': 1.6,
			'omega_3': 49,
			'omega_6': 1589,
			'cholesterol': 0,
			'vitamin a': 214,
			'vitamin c': 0,
			'vitamin d': 0,
			'vitamin e': 0.6,
			'vitamin k': 0.3,
			'thiamin': 0.4,
			'riboflavin': 0.2,
			'niacin': 3.6,
			'vitamin b6': 0.3,
			'folic acid': 25,
			'vitamin b12': 0,
			'biotin': 0,
			'pantothenic acid': 0.4,
			'calcium': 6,
			'iron': 3.5,
			'phosphorus': 241,
			'iodine': 0,
			'magnesium': 127,
			'zinc': 1.8,
			'selenium': 15.5,
			'copper': 0.2,
			'manganese': 0.5,
			'chromium': 0,
			'molybdenum': 0,
			'chloride': 0,
			'potassium': 287,
			'boron': 0,
			'nickel': 0,
			'silicon': 0,
			'tin': 0,
			'vanadium': 0,
			'lycopene': 0,
			'choline': 21.6,
			'sodium': 35
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

	def getX(self):
		return self.x

class YellowCornFlour:
	info = {
		'name': 'Yellow Corn Flour',
		'unit': 'g',
		'size': 22680,
		'price': 37.99,
		'source': 'amazon',
		'link': 'http://amzn.com/B0096QRHM8'
	}

	def __init__(self, x):
		self.nutrition = {
			'calories': 361,
			'carbs': 76.8,
			'fiber': 7.3,
			'protein': 6.9,
			'total_fat': 3.9,
			'saturated_fat': 0.5,
			'monounsaturated_fat': 1,
			'polyunsaturated_fat': 1.8,
			'omega_3': 53,
			'omega_6': 1706,
			'cholesterol': 0,
			'vitamin a': 214,
			'vitamin c': 0,
			'vitamin d': 0,
			'vitamin e': 0.6,
			'vitamin k': 0.3,
			'thiamin': 0.2,
			'riboflavin': 0.1,
			'niacin': 1.9,
			'vitamin b6': 0.4,
			'folic acid': 25,
			'vitamin b12': 0,
			'biotin': 0,
			'pantothenic acid': 0.7,
			'calcium': 7,
			'iron': 2.4,
			'phosphorus': 272,
			'iodine': 0,
			'magnesium': 93,
			'zinc': 1.7,
			'selenium': 15.4,
			'copper': 0.2,
			'manganese': 0.5,
			'chromium': 0,
			'molybdenum': 0,
			'chloride': 0,
			'potassium': 315,
			'boron': 0,
			'nickel': 0,
			'silicon': 0,
			'tin': 0,
			'vanadium': 0,
			'lycopene': 0,
			'choline': 21.6,
			'sodium': 5
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

	def getX(self):
		return self.x

class OatFiber:
	info = {
		'name': 'Oat Fiber',
		'unit': 'g',
		'size': 22680,
		'price': 150.99,
		'source': 'amazon',
		'link': 'http://amzn.com/B0098QIUEA'
	}

	def __init__(self, x):
		self.nutrition = {
			'calories': 20,
			'carbs': 91,
			'fiber': 90,
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
			'calcium': 0.4,
			'iron': 0.48,
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
			'sodium': 40
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

	def getX(self):
		return self.x

class WheyProteinConcentrate80:
	info = {
		'name': 'Whey Protein Concentrate 80%',
		'unit': 'g',
		'size': 20000,
		'price': 371.99,
		'source': 'amazon',
		'link': 'http://amzn.com/B0096R2LQO'
	}

	def __init__(self, x):
		self.nutrition = {
			'calories': 390,
			'carbs': 0,
			'fiber': 0,
			'protein': 80,
			'total_fat': 6,
			'saturated_fat': 2,
			'monounsaturated_fat': 0,
			'polyunsaturated_fat': 0,
			'omega_3': 0,
			'omega_6': 0,
			'cholesterol': 220,
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
			'calcium': 0.60,
			'iron': 0.48,
			'phosphorus': 200,
			'iodine': 0,
			'magnesium': 160,
			'zinc': 0,
			'selenium': 0,
			'copper': 0,
			'manganese': 0,
			'chromium': 0,
			'molybdenum': 0,
			'chloride': 0,
			'potassium': 480,
			'boron': 0,
			'nickel': 0,
			'silicon': 0,
			'tin': 0,
			'vanadium': 0,
			'lycopene': 0,
			'choline': 0,
			'sodium': 180
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

	def getX(self):
		return self.x

class WheyProteinConcentrate34:
	info = {
		'name': 'Whey Protein Concentrate 34%',
		'unit': 'g',
		'size': 22680,
		'price': 162.99,
		'source': 'amazon',
		'link': 'http://amzn.com/B0096R205G'
	}

	def __init__(self, x):
		self.nutrition = {
			'calories': 380,
			'carbs': 51,
			'fiber': 0,
			'protein': 35,
			'total_fat': 3,
			'saturated_fat': 2.5,
			'monounsaturated_fat': 0,
			'polyunsaturated_fat': 0,
			'omega_3': 0,
			'omega_6': 0,
			'cholesterol': 95,
			'vitamin a': 60,
			'vitamin c': 1.8,
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
			'calcium': 0.50,
			'iron': 0.32,
			'phosphorus': 200,
			'iodine': 0,
			'magnesium': 160,
			'zinc': 0,
			'selenium': 0,
			'copper': 0,
			'manganese': 0,
			'chromium': 0,
			'molybdenum': 0,
			'chloride': 0,
			'potassium': 480,
			'boron': 0,
			'nickel': 0,
			'silicon': 0,
			'tin': 0,
			'vanadium': 0,
			'lycopene': 0,
			'choline': 0,
			'sodium': 550
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

	def getX(self):
		return self.x

class WheyProteinIsolate:
	info = {
		'name': 'Whey Protein Isolate',
		'unit': 'g',
		'size': 4540,
		'price': 126.11,
		'source': 'amazon',
		'link': 'http://amzn.com/B000MAK59O'
	}

	def __init__(self, x):
		self.nutrition = {
			'calories': 393,
			'carbs': 0,
			'fiber': 0,
			'protein': 89.3,
			'total_fat': 1.8,
			'saturated_fat': 0,
			'monounsaturated_fat': 0,
			'polyunsaturated_fat': 0,
			'omega_3': 0,
			'omega_6': 0,
			'cholesterol': 17.8,
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
			'calcium': 0.5,
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
			'potassium': 482,
			'boron': 0,
			'nickel': 0,
			'silicon': 0,
			'tin': 0,
			'vanadium': 0,
			'lycopene': 0,
			'choline': 0,
			'sodium': 160
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

	def getX(self):
		return self.x

class IodisedSalt:
	info = {
		'name': 'Iodised Salt',
		'unit': 'g',
		'size': 17688,
		'price': 12,
		'source': 'dollar tree',
		'link': 'http://www.dollartree.com/Royal-Crystal-Iodized-Salt-26-oz-Canisters/p294532/index.pro'
	}

	def __init__(self, x):
		self.nutrition = {
			'calories': 0,
			'carbs': 0,
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
			'iodine': 45000,
			'magnesium': 0,
			'zinc': 0,
			'selenium': 0,
			'copper': 0,
			'manganese': 0,
			'chromium': 0,
			'molybdenum': 0,
			'chloride': 60,
			'potassium': 0,
			'boron': 0,
			'nickel': 0,
			'silicon': 0,
			'tin': 0,
			'vanadium': 0,
			'lycopene': 0,
			'choline': 0,
			'sodium': 400000
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

	def getX(self):
		return self.x

class PotassiumChloride:
	info = {
		'name': 'Potassium Chloride',
		'unit': 'g',
		'size': 5000,
		'price': 83.96,
		'source': 'amazon',
		'link': 'http://amzn.com/B00QT5WNVO'
	}

	def __init__(self, x):
		self.nutrition = {
			'calories': 0,
			'carbs': 0,
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
			'chloride': 48,
			'potassium': 51.85,
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

	def getX(self):
		return self.x

class PotassiumCitrate:
	info = {
		'name': 'Potassium Citrate',
		'unit': 'g',
		'size': 5000,
		'price': 126.96,
		'source': 'amazon',
		'link': 'http://amzn.com/B00PM3FMIK'
	}

	def __init__(self, x):
		self.nutrition = {
			'calories': 0,
			'carbs': 0,
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
			'potassium': 36,
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

	def getX(self):
		return self.x
