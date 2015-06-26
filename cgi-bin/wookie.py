#!/usr/bin/env python
from lib.wookie import Wookie
import sqlite3
import cgi

form = cgi.FieldStorage()
conn = sqlite3.connect('database.db')
c = conn.cursor()
key = (('Calories', ''), ('Carbs', 'g'), ('Fiber', 'g'), ('Protein', 'g'),
	('Total Fat', 'g'), ('Saturated Fat', 'g'), ('Monounsaturated Fat', 'g'),
	('Polyunsaturated Fat', 'g'), ('Omega 3', 'g'), ('Omega 6', 'g'),
	('Cholesterol', 'mg'), ('Vitamin A', ' IU'), ('Vitamin C', 'mg'),
	('Vitamin D', ' IU'), ('Vitamin E', ' IU'), ('Vitamin K', 'mcg'),
	('Thiamin', 'mg'), ('Riboflavin', 'mg'), ('Niacin', 'mg'), ('Vitamin B6', 'mg'),
	('Folate', 'mcg'), ('Vitamin B12', 'mcg'), ('Biotin', 'mcg'),
	('Pantothenic Acid', 'mg'), ('Calcium', 'mg'), ('Iron', 'mg'), ('Phosphorus', 'mg'),
	('Iodine', 'mcg'), ('Magnesium', 'mg'), ('Zinc', 'mg'), ('Selenium', 'mcg'),
	('Copper', 'mg'), ('Manganese', 'mg'), ('Chromium', 'mcg'),
	('Molybdenum', 'mcg'), ('Chloride', 'mg'), ('Potassium', 'mg'),
	('Choline', 'mg'), ('Sodium', 'mg'))

print('Content-type: text/html')
print()
print('<!DOCTYPE html>')
print('<html lang="en">')
print('<head>')
print('	<title>Wookie</title>')
print('	<meta charset="utf-8">')
print('	<meta name="viewport" content="width=device-width, initial-scale=1">')
print('	<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">')
print('	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>')
print('	<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>')
print('</head>')
print('<body>')
print('<div class="container">')
print('	<div class="jumbotron">')
print('		<h1>Wookie</h1>')
print('	</div>')
print('	<form action="/cgi-bin/wookie.py" method="POST">')
print('		<table class="table">')
print('			<thead>')
print('				<tr>')
print('					<th>Profile</th>')
print('				</tr>')
print('			</thead>')
print('			<tbody>')
print('				<tr>')
print('					<td>')
print('						<select name="profile">')

for row in c.execute('SELECT name FROM profiles'):
	print('							<option value="%s">%s</option>' % (row[0], row[0]))

print('						</select>')
print('					</td>')
print('				</tr>')
print('				<tr>')
print('					<td style="text-align: center"><input type="submit" value="Submit"></td>')
print('				</tr>')
print('			</tbody>')
print('		</table>')
print('	</form>')

if 'profile' in form:
	result = Wookie(form.getvalue('profile')).getBest()

	print('	<div style="float: left; width: 60%">')
	print('		<table class="table">')
	print('			<thead>')
	print('				<tr>')
	print('					<th>Recipe</th>')
	print('				</tr>')
	print('			</thead>')
	print('			<tbody>')

	for item in result.getRecipe():
		print('				<tr>')
		print('					<td>%s</td>' % (item))
		print('				</tr>')

	print('			</tbody>')
	print('		</table>')
	print('	</div>')
	print('	<div style="float: right; width: 35%">')
	print('		<table class="table">')
	print('			<thead>')
	print('				<tr>')
	print('					<th>Nutrition Facts</th>')
	print('				</tr>')
	print('			</thead>')
	print('			<tbody>')

	stats = result.getStats()
	for x in range(39):
		print('				<tr>')
		print('					<td>%s</td>' % (key[x][0]))
		print('					<td style="text-align: right">%.2f%s</td>' % (stats[x], key[x][1]))
		print('				</tr>')

	print('			</tbody>')
	print('		</table>')
	print('	</div>')
	print('	<h2 style="text-align: center; padding-top: 1em; clear: both">%.2f%% different</h2>' % (result.getPercent()))
	print('	<h2 style="text-align: center; padding-bottom: 1em">$%.2f per day</h2>' % (result.getPrice()))

print('	<div class="row">')
print('		<footer style="text-align: center">')
print('			<p>Copyright 2015 Justin Willis</p>')
print('			<a href="https://github.com/bkvaluemeal/north-american-wookie" class="btn btn-link" role="button">GitHub</a>')
print('		</footer>')
print('	</div>')
print('</div>')
print('</body>')
print('</html>')
