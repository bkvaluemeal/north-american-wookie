#!/usr/bin/env python
from lib import label
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()
profiles = ()
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
print('	<title>Profles</title>')
print('	<meta charset="utf-8">')
print('	<meta name="viewport" content="width=device-width, initial-scale=1">')
print('	<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">')
print('	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>')
print('	<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>')
print('</head>')
print('<body>')
print('<div class="container">')
print('	<div class="jumbotron">')
print('		<h1>Profiles</h1>')
print('	</div>')
print('	<table class="table table-hover">')
print('		<thead>')
print('			<tr>')
print('				<th>Name</th>')
print('			</tr>')
print('		</thead>')
print('		<tbody>')

for row in c.execute('SELECT * FROM profiles'):
	print('			<tr data-toggle="modal" data-target="#%s">' % (row[0].lower().replace(' ', '-')))
	print('				<td>%s</td>' % (row[0]))
	print('			</tr>')
	profiles += ((row),)

print('		</tbody>')
print('	</table>')

for profile in profiles:
	print('	<div class="modal fade" id="%s" role="dialog">' % (profile[0].lower().replace(' ', '-')))
	print('		<div class="modal-dialog" style="width: 90%">')
	print('			<div class="modal-content">')
	print('				<div class="modal-header">')
	print('					<button type="button" class="close" data-dismiss="modal">&times;</button>')
	print('					<h4 class="modal-title">%s</h4>' % (profile[0]))
	print('				</div>')
	print('				<div class="modal-body">')
	print('					<table class="table">')
	print('						<thead>')
	print('							<tr>')
	print('								<th>Macro Nutrients</th>')
	print('								<th style="text-align: right">Amount</th>')
	print('								<th></th>')
	print('								<th>Vitamins</th>')
	print('								<th style="text-align: right">Amount</th>')
	print('								<th></th>')
	print('								<th>Minerals</th>')
	print('								<th style="text-align: right">Amount</th>')
	print('							</tr>')
	print('						</thead>')
	print('						<tbody>')

	for x in range(15):
		print('							<tr>')

		if x < 11:
			print('								<td>%s</td>' % (key[x][0]))
			print('								<td style="text-align: right">%.1f%s</td>' % (profile[x + 1], key[x][1]))
		else:
			print('								<td></td>')
			print('								<td></td>')

		print('								<td></td>')

		if x < 12:
			print('								<td>%s</td>' % (key[x + 11][0]))
			print('								<td style="text-align: right">%.1f%s</td>' % (profile[x + 12], key[x + 11][1]))
		else:
			print('								<td></td>')
			print('								<td></td>')

		print('								<td></td>')
		print('								<td>%s</td>' % (key[x + 24][0]))
		print('								<td style="text-align: right">%.1f%s</td>' % (profile[x + 25], key[x + 24][1]))
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
