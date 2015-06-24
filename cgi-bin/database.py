#!/usr/bin/env python
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()
ingredients = ()
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
print('	<title>Database</title>')
print('	<meta charset="utf-8">')
print('	<meta name="viewport" content="width=device-width, initial-scale=1">')
print('	<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">')
print('	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>')
print('	<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>')
print('</head>')
print('<body>')
print('<div class="container">')
print('	<div class="jumbotron">')
print('		<h1>Database</h1>')
print('	</div>')
print('	<table class="table table-hover">')
print('		<thead>')
print('			<tr>')
print('				<th>Name</th>')
print('				<th>Size</th>')
print('				<th>Price</th>')
print('				<th>Source</th>')
print('			</tr>')
print('		</thead>')
print('		<tbody>')

for row in c.execute('SELECT * FROM ingredients'):
	print('			<tr data-toggle="modal" data-target="#%s">' % (row[0].lower().replace(' ', '-')))
	print('				<td>%s</td>' % (row[0]))
	print('				<td>%i%s</td>' % (row[1], row[2]))
	print('				<td>$%.2f</td>' % (row[3]))
	print('				<td><a href="%s">%s</a></td>' % (row[4], row[5]))
	print('			</tr>')
	ingredients += ((row[0],) + (row[6:]),)

print('		</tbody>')
print('	</table>')

for ingredient in ingredients:
	print('	<div class="modal fade" id="%s" role="dialog">' % (ingredient[0].lower().replace(' ', '-')))
	print('		<div class="modal-dialog modal-sm">')
	print('			<div class="modal-content">')
	print('				<div class="modal-header">')
	print('					<button type="button" class="close" data-dismiss="modal">&times;</button>')
	print('					<h4 class="modal-title">%s</h4>' % (ingredient[0]))
	print('				</div>')
	print('				<div class="modal-body">')
	print('					<table class="table">')
	print('						<thead>')
	print('							<tr>')
	print('								<th>Nutrient</th>')
	print('								<th style="text-align: right">Amount</th>')
	print('							</tr>')
	print('						</thead>')
	print('						<tbody>')

	for x in range(39):
		print('							<tr>')
		print('								<td>%s</td>' % (key[x][0]))
		print('								<td style="text-align: right">%.0f%s</td>' % (ingredient[x + 1], key[x][1]))
		print('							</tr>')

	print('						</tbody>')
	print('					</table>')
	print('				</div>')
	print('				<div class="modal-footer">')
	print('					<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>')
	print('				</div>')
	print('			</div>')
	print('		</div>')
	print('	</div>')

print('	<div class="row">')
print('		<footer style="text-align: center">')
print('			<p>Copyright 2015 Justin Willis</p>')
print('			<a href="https://github.com/bkvaluemeal/north-american-wookie" class="btn btn-link" role="button">GitHub</a>')
print('		</footer>')
print('	</div>')
print('</div>')
print('</body>')
print('</html>')
