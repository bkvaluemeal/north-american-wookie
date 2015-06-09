import ingredients
import random

stat = {'calories': 0, 'carbs': 0, 'fiber': 0, 'protein': 0, 'total_fat': 0,
	'saturated_fat': 0, 'monounsaturated_fat': 0, 'polyunsaturated_fat': 0,
	'omega_3': 0, 'omega_6': 0, 'cholesterol': 0, 'vitamin a': 0,
	'vitamin c': 0, 'vitamin d': 0, 'vitamin e': 0, 'vitamin k': 0,
	'thiamin': 0, 'riboflavin': 0, 'niacin': 0, 'vitamin b6': 0,
	'folic acid': 0, 'vitamin b12': 0, 'biotin': 0, 'pantothenic acid': 0,
	'calcium': 0, 'iron': 0, 'phosphorus': 0, 'iodine': 0, 'magnesium': 0,
	'zinc': 0, 'selenium': 0, 'copper': 0, 'manganese': 0, 'chromium': 0,
	'molybdenum': 0, 'chloride': 0, 'potassium': 0, 'boron': 0, 'nickel': 0,
	'silicon': 0, 'tin': 0, 'vanadium': 0, 'lycopene': 0, 'choline': 0}
recipe = {}
price = 0

for ingredient in dir(ingredients)[:-8]:
	x = random.randint(0, 1000)

	if x == 0:
		continue

	temp = getattr(ingredients, ingredient)(x)
	recipe[temp.getName() + ' ' + str(x) + temp.getUnit()] = temp

for ammount, item in recipe.items():
	print(ammount)
	for key, value in item.getNutrition().items():
		stat[key] += value
	price += item.getPrice()

print()
print('$' + str(round(price, 2)) + ' per day')
print()
print('+---------------------------------------+')
print('|            Nutrition Facts            |')
print('+---------------------------------------+')
print('| %-37s |' % ('Calories ' + str(round(stat['calories'], 2))))
print('+---------------------------------------+')
print('| %-29s %6s%% |' % ('Carbohydrates ' + str(round(stat['carbs'], 2)) + 'g', round(stat['carbs'] / 250 * 100, 2)))
print('| %-29s %6s%% |' % ('  Fiber ' + str(round(stat['fiber'], 2)) + 'g', round(stat['fiber'] / 28 * 100, 2)))
print('| %-29s %6s%% |' % ('Protein ' + str(round(stat['protein'], 2)) + 'g', round(stat['protein'] / 85 * 100, 2)))
print('| %-29s %6s%% |' % ('Total Fat '+ str(round(stat['total_fat'], 2)) + 'g', round(stat['total_fat'] / 65 * 100)))
print('|   %-35s |' % ('Saturated Fat ' + str(round(stat['saturated_fat'], 2)) + 'g'))
print('|   %-35s |' % ('Monounsaturated Fat ' + str(round(stat['monounsaturated_fat'], 2)) + 'g'))
print('|   %-35s |' % ('Polyunsaturated Fat ' + str(round(stat['polyunsaturated_fat'], 2)) + 'g'))
print('|   %-27s %6s%% |' % ('Omega-3 Fatty Acids ' + str(round(stat['omega_3'], 2)) + 'g', round(stat['omega_3'] / 1.6 * 100)))
print('|   %-27s %6s%% |' % ('Omega-6 Fatty Acids ' + str(round(stat['omega_6'], 2)) + 'g', round(stat['omega_6'] / 17 * 100)))
print('| %-37s |' % ('Cholesterol ' + str(round(stat['cholesterol'], 2)) + 'mg'))
print('+---------------------------------------+')
print('| %-29s %6s%% |' % ('Vitamin A ' + str(round(stat['vitamin a'], 2)) + ' IU', round(stat['vitamin a'] / 3000 * 100, 2)))
print('| %-29s %6s%% |' % ('Vitamin C ' + str(round(stat['vitamin c'], 2)) + 'mg', round(stat['vitamin c'] / 90 * 100, 2)))
print('| %-29s %6s%% |' % ('Vitamin D ' + str(round(stat['vitamin d'], 2)) + ' IU', round(stat['vitamin d'] / 600 * 100, 2)))
print('| %-29s %6s%% |' % ('Vitamin E ' + str(round(stat['vitamin e'], 2)) + ' IU', round(stat['vitamin e'] / 20 * 100, 2)))
print('| %-29s %6s%% |' % ('Vitamin K ' + str(round(stat['vitamin k'], 2)) + 'mcg', round(stat['vitamin k'] / 120 * 100, 2)))
print('| %-29s %6s%% |' % ('Thiamin ' + str(round(stat['thiamin'], 2)) + 'mg', round(stat['thiamin'] / 1.2 * 100, 2)))
print('| %-29s %6s%% |' % ('Riboflavin ' + str(round(stat['riboflavin'], 2)) + 'mg', round(stat['riboflavin'] / 1.3 * 100, 2)))
print('| %-29s %6s%% |' % ('Niacin ' + str(round(stat['niacin'], 2)) + 'mg', round(stat['niacin'] / 16 * 100, 2)))
print('| %-29s %6s%% |' % ('Vitamin B6 ' + str(round(stat['vitamin b6'], 2)) + 'mg', round(stat['vitamin b6'] / 1.3 * 100, 2)))
print('| %-29s %6s%% |' % ('Folic Acid ' + str(round(stat['folic acid'], 2)) + 'mcg', round(stat['folic acid'] / 400 * 100, 2)))
print('| %-29s %6s%% |' % ('Vitamin B12 ' + str(round(stat['vitamin b12'], 2)) + 'mcg', round(stat['vitamin b12'] / 2.4 * 100, 2)))
print('| %-29s %6s%% |' % ('Biotin ' + str(round(stat['biotin'], 2)) + 'mcg', round(stat['biotin'] / 30 * 100, 2)))
print('| %-29s %6s%% |' % ('Pantothenic Acid ' + str(round(stat['pantothenic acid'], 2)) + 'mg', round(stat['pantothenic acid'] / 5 * 100, 2)))
print('| %-29s %6s%% |' % ('Calcium ' + str(round(stat['calcium'], 2)) + 'mg', round(stat['calcium'] / 1 * 100, 2)))
print('| %-29s %6s%% |' % ('Iron ' + str(round(stat['iron'], 2)) + 'mg', round(stat['iron'] / 8 * 100, 2)))
print('| %-29s %6s%% |' % ('Phosphorus ' + str(round(stat['phosphorus'], 2)) + 'mg', round(stat['phosphorus'] / 700 * 100, 2)))
print('| %-29s %6s%% |' % ('Iodine ' + str(round(stat['iodine'], 2)) + 'mcg', round(stat['iodine'] / 150 * 100, 2)))
print('| %-29s %6s%% |' % ('Magnesium ' + str(round(stat['magnesium'], 2)) + 'mg', round(stat['magnesium'] / 420 * 100, 2)))
print('| %-29s %6s%% |' % ('Zinc ' + str(round(stat['zinc'], 2)) + 'mg', round(stat['zinc'] / 11 * 100, 2)))
print('| %-29s %6s%% |' % ('Selenium ' + str(round(stat['selenium'], 2)) + 'mcg', round(stat['selenium'] / 55 * 100, 2)))
print('| %-29s %6s%% |' % ('Copper ' + str(round(stat['copper'], 2)) + 'mg', round(stat['copper'] / 0.9 * 100, 2)))
print('| %-29s %6s%% |' % ('Manganese ' + str(round(stat['manganese'], 2)) + 'mg', round(stat['manganese'] / 2.3 * 100, 2)))
print('| %-29s %6s%% |' % ('Chromium ' + str(round(stat['chromium'], 2)) + 'mcg', round(stat['chromium'] / 35 * 100, 2)))
print('| %-29s %6s%% |' % ('Molybdenum ' + str(round(stat['molybdenum'], 2)) + 'mcg', round(stat['molybdenum'] / 45 * 100, 2)))
print('| %-29s %6s%% |' % ('Chloride ' + str(round(stat['chloride'], 2)) + 'mg', round(stat['chloride'] / 2.3 * 100, 2)))
print('| %-29s %6s%% |' % ('Potassium ' + str(round(stat['potassium'], 2)) + 'mg', round(stat['potassium'] / 3.5 * 100, 2)))
print('| %-29s %6s%% |' % ('Boron ' + str(round(stat['boron'], 2)) + 'mcg', round(stat['boron'] / 0.25 * 100, 2)))
print('| %-29s %6s%% |' % ('Nickel ' + str(round(stat['nickel'], 2)) + 'mcg', round(stat['nickel'] / 5 * 100, 2)))
print('| %-29s %6s%% |' % ('Silicon ' + str(round(stat['silicon'], 2)) + 'mg', round(stat['silicon'] / 2 * 100, 2)))
print('| %-29s %6s%% |' % ('Tin ' + str(round(stat['tin'], 2)) + 'mcg', round(stat['tin'] / 10 * 100, 2)))
print('| %-29s %6s%% |' % ('Vanadium ' + str(round(stat['vanadium'], 2)) + 'mcg', round(stat['vanadium'] / 10 * 100, 2)))
print('| %-29s %6s%% |' % ('Lycopene ' + str(round(stat['lycopene'], 2)) + 'mcg', round(stat['lycopene'] / 600 * 100, 2)))
print('| %-29s %6s%% |' % ('Choline ' + str(round(stat['choline'], 2)) + 'mg', round(stat['choline'] / 550 * 100, 2)))
print('+---------------------------------------+')
