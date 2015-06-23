import sqlite3
import random
import copy

conn = sqlite3.connect('database.db')
c = conn.cursor()

class Recipe:
	def __init__(self):
		self.stat = [0 for x in range(45)]
		self.recipe = ()
		self.price = 0

		for ingredient in c.execute('SELECT * FROM ingredients'):
			x = random.uniform(0.0, 500.0)

			if x == 0:
				continue

			self.recipe += ((ingredient[0], x, ingredient[2]),)

			for y in range(45):
				self.stat[y] += ingredient[6:][y] * x / 100

			self.price += (x / ingredient[1]) * ingredient[3]

	def getStats(self):
		return self.stat

	def getRecipe(self, verbose = False):
		if verbose:
			return self.recipe
		else:
			result = ()

			for item in self.recipe:
				result += ('%s %.1f%s' % (item[0], item[1], item[2]),)

			return result

	def getPrice(self):
		return round(self.price, 2)

	def getPercent(self):
		return 0

	def mutate(self):
		self.stat = [0 for x in range(45)]
		result = ()
		self.price = 0

		for item in self.recipe:
			x = item[1] * random.uniform(0.95, 1.05)

			if x < 1:
				continue

			for ingredient in c.execute('SELECT * FROM ingredients WHERE name = ?', (item[0],)):
				result += ((ingredient[0], x, ingredient[2]),)

				for y in range(45):
					self.stat[y] += ingredient[6:][y] * x / 100

				self.price += (x / ingredient[1]) * ingredient[3]

		self.recipe = result

recipes = (Recipe() for x in range(100))
most_fit = None

for x in recipes:
	print('[0] ' + str(x.getPercent()))

	if most_fit == None or (x.getPercent() < most_fit.getPercent() and x.getPercent() >= 0):
		most_fit = x

for gen in range(1, 101):
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
