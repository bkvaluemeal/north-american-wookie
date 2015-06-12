import ingredients
import random
import copy

def printLabel(stat):
	print('+---------------------------------------+')
	print('|            Nutrition Facts            |')
	print('+---------------------------------------+')
	print('| %-37s |' % ('Calories ' + str(round(stat['calories'], 2))))
	print('+---------------------------------------+')
	print('| %-28s %7s%% |' % ('Carbohydrates ' + str(round(stat['carbs'], 2)) + 'g', round(stat['carbs'] / 250 * 100, 2)))
	print('| %-28s %7s%% |' % ('  Fiber ' + str(round(stat['fiber'], 2)) + 'g', round(stat['fiber'] / 28 * 100, 2)))
	print('| %-28s %7s%% |' % ('Protein ' + str(round(stat['protein'], 2)) + 'g', round(stat['protein'] / 85 * 100, 2)))
	print('| %-28s %7s%% |' % ('Total Fat '+ str(round(stat['total_fat'], 2)) + 'g', round(stat['total_fat'] / 65 * 100, 2)))
	print('|   %-35s |' % ('Saturated Fat ' + str(round(stat['saturated_fat'], 2)) + 'g'))
	print('|   %-35s |' % ('Monounsaturated Fat ' + str(round(stat['monounsaturated_fat'], 2)) + 'g'))
	print('|   %-35s |' % ('Polyunsaturated Fat ' + str(round(stat['polyunsaturated_fat'], 2)) + 'g'))
	print('|   %-26s %7s%% |' % ('Omega-3 Fatty Acids ' + str(round(stat['omega_3'], 2)) + 'g', round(stat['omega_3'] / 1.6 * 100, 2)))
	print('|   %-26s %7s%% |' % ('Omega-6 Fatty Acids ' + str(round(stat['omega_6'], 2)) + 'g', round(stat['omega_6'] / 17 * 100, 2)))
	print('| %-37s |' % ('Cholesterol ' + str(round(stat['cholesterol'], 2)) + 'mg'))
	print('+---------------------------------------+')
	print('| %-28s %7s%% |' % ('Vitamin A ' + str(round(stat['vitamin a'], 2)) + ' IU', round(stat['vitamin a'] / 3000 * 100, 2)))
	print('| %-28s %7s%% |' % ('Vitamin C ' + str(round(stat['vitamin c'], 2)) + 'mg', round(stat['vitamin c'] / 90 * 100, 2)))
	print('| %-28s %7s%% |' % ('Vitamin D ' + str(round(stat['vitamin d'], 2)) + ' IU', round(stat['vitamin d'] / 600 * 100, 2)))
	print('| %-28s %7s%% |' % ('Vitamin E ' + str(round(stat['vitamin e'], 2)) + ' IU', round(stat['vitamin e'] / 20 * 100, 2)))
	print('| %-28s %7s%% |' % ('Vitamin K ' + str(round(stat['vitamin k'], 2)) + 'mcg', round(stat['vitamin k'] / 120 * 100, 2)))
	print('| %-28s %7s%% |' % ('Thiamin ' + str(round(stat['thiamin'], 2)) + 'mg', round(stat['thiamin'] / 1.2 * 100, 2)))
	print('| %-28s %7s%% |' % ('Riboflavin ' + str(round(stat['riboflavin'], 2)) + 'mg', round(stat['riboflavin'] / 1.3 * 100, 2)))
	print('| %-28s %7s%% |' % ('Niacin ' + str(round(stat['niacin'], 2)) + 'mg', round(stat['niacin'] / 16 * 100, 2)))
	print('| %-28s %7s%% |' % ('Vitamin B6 ' + str(round(stat['vitamin b6'], 2)) + 'mg', round(stat['vitamin b6'] / 1.3 * 100, 2)))
	print('| %-28s %7s%% |' % ('Folic Acid ' + str(round(stat['folic acid'], 2)) + 'mcg', round(stat['folic acid'] / 400 * 100, 2)))
	print('| %-28s %7s%% |' % ('Vitamin B12 ' + str(round(stat['vitamin b12'], 2)) + 'mcg', round(stat['vitamin b12'] / 2.4 * 100, 2)))
	print('| %-28s %7s%% |' % ('Biotin ' + str(round(stat['biotin'], 2)) + 'mcg', round(stat['biotin'] / 30 * 100, 2)))
	print('| %-28s %7s%% |' % ('Pantothenic Acid ' + str(round(stat['pantothenic acid'], 2)) + 'mg', round(stat['pantothenic acid'] / 5 * 100, 2)))
	print('| %-28s %7s%% |' % ('Calcium ' + str(round(stat['calcium'], 2)) + 'mg', round(stat['calcium'] / 1 * 100, 2)))
	print('| %-28s %7s%% |' % ('Iron ' + str(round(stat['iron'], 2)) + 'mg', round(stat['iron'] / 8 * 100, 2)))
	print('| %-28s %7s%% |' % ('Phosphorus ' + str(round(stat['phosphorus'], 2)) + 'mg', round(stat['phosphorus'] / 700 * 100, 2)))
	print('| %-28s %7s%% |' % ('Iodine ' + str(round(stat['iodine'], 2)) + 'mcg', round(stat['iodine'] / 150 * 100, 2)))
	print('| %-28s %7s%% |' % ('Magnesium ' + str(round(stat['magnesium'], 2)) + 'mg', round(stat['magnesium'] / 420 * 100, 2)))
	print('| %-28s %7s%% |' % ('Zinc ' + str(round(stat['zinc'], 2)) + 'mg', round(stat['zinc'] / 11 * 100, 2)))
	print('| %-28s %7s%% |' % ('Selenium ' + str(round(stat['selenium'], 2)) + 'mcg', round(stat['selenium'] / 55 * 100, 2)))
	print('| %-28s %7s%% |' % ('Copper ' + str(round(stat['copper'], 2)) + 'mg', round(stat['copper'] / 0.9 * 100, 2)))
	print('| %-28s %7s%% |' % ('Manganese ' + str(round(stat['manganese'], 2)) + 'mg', round(stat['manganese'] / 2.3 * 100, 2)))
	print('| %-28s %7s%% |' % ('Chromium ' + str(round(stat['chromium'], 2)) + 'mcg', round(stat['chromium'] / 35 * 100, 2)))
	print('| %-28s %7s%% |' % ('Molybdenum ' + str(round(stat['molybdenum'], 2)) + 'mcg', round(stat['molybdenum'] / 45 * 100, 2)))
	print('| %-28s %7s%% |' % ('Chloride ' + str(round(stat['chloride'], 2)) + 'mg', round(stat['chloride'] / 2.3 * 100, 2)))
	print('| %-28s %7s%% |' % ('Potassium ' + str(round(stat['potassium'], 2)) + 'mg', round(stat['potassium'] / 3.5 * 100, 2)))
	print('| %-28s %7s%% |' % ('Boron ' + str(round(stat['boron'], 2)) + 'mcg', round(stat['boron'] / 0.25 * 100, 2)))
	print('| %-28s %7s%% |' % ('Nickel ' + str(round(stat['nickel'], 2)) + 'mcg', round(stat['nickel'] / 5 * 100, 2)))
	print('| %-28s %7s%% |' % ('Silicon ' + str(round(stat['silicon'], 2)) + 'mg', round(stat['silicon'] / 2 * 100, 2)))
	print('| %-28s %7s%% |' % ('Tin ' + str(round(stat['tin'], 2)) + 'mcg', round(stat['tin'] / 10 * 100, 2)))
	print('| %-28s %7s%% |' % ('Vanadium ' + str(round(stat['vanadium'], 2)) + 'mcg', round(stat['vanadium'] / 10 * 100, 2)))
	print('| %-28s %7s%% |' % ('Lycopene ' + str(round(stat['lycopene'], 2)) + 'mcg', round(stat['lycopene'] / 600 * 100, 2)))
	print('| %-28s %7s%% |' % ('Choline ' + str(round(stat['choline'], 2)) + 'mg', round(stat['choline'] / 550 * 100, 2)))
	print('| %-28s %7s%% |' % ('Sodium ' + str(round(stat['sodium'], 2)) + 'mg', round(stat['sodium'] / 1500 * 100, 2)))
	print('+---------------------------------------+')

class Recipe:
	def __init__(self):
		self.stat = {'calories': 0, 'carbs': 0, 'fiber': 0, 'protein': 0, 'total_fat': 0,
			'saturated_fat': 0, 'monounsaturated_fat': 0, 'polyunsaturated_fat': 0,
			'omega_3': 0, 'omega_6': 0, 'cholesterol': 0, 'vitamin a': 0,
			'vitamin c': 0, 'vitamin d': 0, 'vitamin e': 0, 'vitamin k': 0,
			'thiamin': 0, 'riboflavin': 0, 'niacin': 0, 'vitamin b6': 0,
			'folic acid': 0, 'vitamin b12': 0, 'biotin': 0, 'pantothenic acid': 0,
			'calcium': 0, 'iron': 0, 'phosphorus': 0, 'iodine': 0, 'magnesium': 0,
			'zinc': 0, 'selenium': 0, 'copper': 0, 'manganese': 0, 'chromium': 0,
			'molybdenum': 0, 'chloride': 0, 'potassium': 0, 'boron': 0, 'nickel': 0,
			'silicon': 0, 'tin': 0, 'vanadium': 0, 'lycopene': 0, 'choline': 0,
			'sodium': 0}
		self.recipe = {}
		self.price = 0

		for ingredient in dir(ingredients)[:-8]:
			x = round(random.uniform(0.0, 500.0), 1)

			if x == 0:
				continue

			temp = getattr(ingredients, ingredient)(x)
			self.recipe[temp.getName() + ' ' + str(x) + temp.getUnit()] = temp

		for ammount, item in self.recipe.items():
			for key, value in item.getNutrition().items():
				self.stat[key] += value
			self.price += item.getPrice()

	def getStats(self):
		return self.stat

	def getRecipe(self):
		return self.recipe

	def getPrice(self):
		return round(self.price, 2)

	def getPercent(self):
		result = 0
		result += abs(self.stat['calories'] - 2000) / 2000 * 100
		result += abs(self.stat['carbs'] - 250) / 250 * 100
		result += abs(self.stat['fiber'] - 28) / 28 * 100
		result += abs(self.stat['protein'] - 85) / 85 * 100
		result += abs(self.stat['total_fat'] - 65) / 65 * 100
		result += abs(self.stat['vitamin a'] - 3000) / 3000 * 100
		result += abs(self.stat['vitamin c'] - 90) / 90 * 100
		result += abs(self.stat['vitamin d'] - 600) / 600 * 100
		result += abs(self.stat['vitamin e'] - 20) / 20 * 100
		result += abs(self.stat['vitamin k'] - 120) / 120 * 100
		result += abs(self.stat['thiamin'] - 1.2) / 1.2 * 100
		result += abs(self.stat['riboflavin'] - 1.3) / 1.3 * 100
		result += abs(self.stat['niacin'] - 16) / 16 * 100
		result += abs(self.stat['vitamin b6'] - 1.3) / 1.3 * 100
		result += abs(self.stat['folic acid'] - 400) / 400 * 100
		result += abs(self.stat['vitamin b12'] - 2.4) / 2.4 * 100
		result += abs(self.stat['biotin'] - 30) / 30 * 100
		result += abs(self.stat['pantothenic acid'] - 5) / 5 * 100
		result += abs(self.stat['calcium'] - 1) / 1 * 100
		result += abs(self.stat['iron'] - 8) / 8 * 100
		result += abs(self.stat['phosphorus'] - 700) / 700 * 100
		result += abs(self.stat['iodine'] - 150) / 150 * 100
		result += abs(self.stat['magnesium'] - 420) / 420 * 100
		result += abs(self.stat['zinc'] - 11) / 11 * 100
		result += abs(self.stat['selenium'] - 55) / 55 * 100
		result += abs(self.stat['copper'] - 0.9) / 0.9 * 100
		result += abs(self.stat['manganese'] - 2.3) / 2.3 * 100
		result += abs(self.stat['chromium'] - 35) / 35 * 100
		result += abs(self.stat['molybdenum'] - 45) / 45 * 100
		result += abs(self.stat['chloride'] - 2.3) / 2.3 * 100
		result += abs(self.stat['potassium'] - 3.5) / 3.5 * 100
		result += abs(self.stat['boron'] - 0.25) / 0.25 * 100
		result += abs(self.stat['nickel'] - 5) / 5 * 100
		result += abs(self.stat['silicon'] - 2) / 2 * 100
		result += abs(self.stat['tin'] - 10) / 10 * 100
		result += abs(self.stat['vanadium'] - 10) / 10 * 100
		result += abs(self.stat['lycopene'] - 600) / 600 * 100
		result += abs(self.stat['choline'] - 550) / 550 * 100
		result += abs(self.stat['sodium'] - 1500) / 1500 * 100

		return result / 39

	def mutate(self):
		result = {}

		for ammount, item in self.recipe.items():
			ingredient = self.recipe[ammount]
			x = round(ingredient.getX() * random.uniform(0.95, 1.05), 1)
			temp = type(ingredient)(x)
			result[temp.getName() + ' ' + str(x) + temp.getUnit()] = temp

		self.recipe = result
		self.stat = {'calories': 0, 'carbs': 0, 'fiber': 0, 'protein': 0, 'total_fat': 0,
			'saturated_fat': 0, 'monounsaturated_fat': 0, 'polyunsaturated_fat': 0,
			'omega_3': 0, 'omega_6': 0, 'cholesterol': 0, 'vitamin a': 0,
			'vitamin c': 0, 'vitamin d': 0, 'vitamin e': 0, 'vitamin k': 0,
			'thiamin': 0, 'riboflavin': 0, 'niacin': 0, 'vitamin b6': 0,
			'folic acid': 0, 'vitamin b12': 0, 'biotin': 0, 'pantothenic acid': 0,
			'calcium': 0, 'iron': 0, 'phosphorus': 0, 'iodine': 0, 'magnesium': 0,
			'zinc': 0, 'selenium': 0, 'copper': 0, 'manganese': 0, 'chromium': 0,
			'molybdenum': 0, 'chloride': 0, 'potassium': 0, 'boron': 0, 'nickel': 0,
			'silicon': 0, 'tin': 0, 'vanadium': 0, 'lycopene': 0, 'choline': 0,
			'sodium': 0}
		self.price = 0

		for ammount, item in self.recipe.items():
			for key, value in item.getNutrition().items():
				self.stat[key] += value
			self.price += item.getPrice()

##############
## Genetics ##
##############

recipes = (Recipe() for x in range(100))
most_fit = None

for x in recipes:
	print('[0] ' + str(x.getPercent()))

	if most_fit == None or (x.getPercent() < most_fit.getPercent() and x.getPercent() >= 0):
		most_fit = x

for gen in range(101):
	recipes = []
	for x in range(100):
		temp = copy.copy(most_fit)
		temp.mutate()
		recipes.append(temp)

	best = None

	for x in recipes:
		print('[' + str(gen) + '] ' + str(x.getPercent()))

		if best == None or (x.getPercent() < best.getPercent() and x.getPercent() >= 0):
			best = x

	most_fit = best

print()
print('[Result] ' + str(most_fit.getPercent()))
print()
for x in most_fit.getRecipe():
	print(x)
print()
print('$' + str(most_fit.getPrice()))
print()
printLabel(most_fit.getStats())
