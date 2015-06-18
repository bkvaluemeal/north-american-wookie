import sqlite3
import ingredients

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute("CREATE TABLE ingredients (name, size, unit, price, link, source, calories, carbs, fiber, protein, total_fat, saturated_fat, monounsaturated_fat, polyunsaturated_fat, omega_3, omega_6, cholesterol, vitamin_a, vitamin_c, vitamin_d, vitamin_e, vitamin_k, thiamin, riboflavin, niacin, vitamin_b6, folate, vitamin_b12, biotin, pantothenic_acid, calcium, iron, phosphorus, iodine, magnesium, zinc, selenium, copper, manganese, chromium, molybdenum, chloride, potassium, boron, nickel, silicon, tin, vanadium, lycopene, choline, sodium)")
for ingredient in dir(ingredients)[:-8]:
	temp = getattr(ingredients, ingredient)(100)
	x = temp.getInfo()
	y = temp.getNutrition()
	c.execute("INSERT INTO ingredients VALUES ('%s', %i, '%s', %f, '%s', '%s', %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f)"
		%
		(x['name'], x['size'], x['unit'], x['price'], x['link'], x['source'].title(), y['calories'], y['carbs'], y['fiber'], y['protein'], y['total_fat'], y['saturated_fat'], y['monounsaturated_fat'], y['polyunsaturated_fat'], y['omega_3'], y['omega_6'], y['cholesterol'], y['vitamin a'], y['vitamin c'], y['vitamin d'], y['vitamin e'], y['vitamin k'], y['thiamin'], y['riboflavin'], y['niacin'], y['vitamin b6'], y['folic acid'], y['vitamin b12'], y['biotin'], y['pantothenic acid'], y['calcium'], y['iron'], y['phosphorus'], y['iodine'], y['magnesium'], y['zinc'], y['selenium'], y['copper'], y['manganese'], y['chromium'], y['molybdenum'], y['chloride'], y['potassium'], y['boron'], y['nickel'], y['silicon'], y['tin'], y['vanadium'], y['lycopene'], y['choline'], y['sodium']))

conn.commit()

for row in c.execute('SELECT * FROM ingredients'):
	print(row)

conn.close()
