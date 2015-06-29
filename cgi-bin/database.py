#!/usr/bin/env python
import sqlite3
import cgi

form = cgi.FieldStorage()
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

def doForm():
	if 'action' in form:
		action = form.getvalue('action')
		stats = ()

		try:
			stats += (form.getvalue('name'),)
			stats += (float(form.getvalue('size')),)
			stats += (form.getvalue('unit'),)
			stats += (float(form.getvalue('price')),)
			stats += (form.getvalue('link'),)
			stats += (form.getvalue('source'),)
		except:
			return 1

		for stat in key:
			try:
				stats += (float(form.getvalue(stat[0].lower().replace(' ', '-'))),)
			except:
				stats += (0,)

		if action == 'add':
			c.execute("INSERT INTO ingredients VALUES ('%s', %f, '%s', %f, '%s', '%s', %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f)" % stats)

		conn.commit()

	return 0

# 0: No error
# 1: Missing form data
error = doForm()

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

if error == 1:
	print('	<h2 style="color: red; text-align: center">Missing form data</h2>')

print('	<button type="button" class="btn btn-sm btn-success" style="margin-bottom: 2em" data-toggle="modal" data-target="#add">Add</button>')
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
print('	<form action="/cgi-bin/database.py" method="POST">')
print('		<input type="hidden" name="action" value="add">')
print('		<div id="add" class="modal fade" role="dialog">')
print('			<div class="modal-dialog" style="width: 90%">')
print('				<div class="modal-content">')
print('					<div class="modal-header">')
print('						<button type="button" class="close" data-dismiss="modal">&times;</button>')
print('						<h4 class="modal-title"><input type="text" name="name" placeholder="New Ingredient" tabindex=1></h4>')
print('					</div>')
print('					<div class="modal-body">')
print('						<table width="100%">')
print('							<tr>')
print('								<td style="white-space: nowrap; padding: 8px">')
print('									<span>Size:</span>')
print('									<input type="text" name="size" size="5" tabindex=2>')
print('									<select name="unit" tabindex=3>')
print('										<option value="g">g</option>')
print('										<option value="ml">ml</option>')
print('									</select>')
print('								</td>')
print('								<td style="white-space: nowrap; padding: 8px">')
print('									<span>Price: $</span>')
print('									<input type="text" name="price" size="5" tabindex=4>')
print('								</td>')
print('								<td style="white-space: nowrap; padding: 8px">')
print('									<span>Link:</span>')
print('									<input type="text" name="link" size="100%" tabindex=5>')
print('								</td>')
print('								<td style="white-space: nowrap; padding: 8px">')
print('									<span>Source:</span>')
print('									<input type="text" name="source" size="100%" tabindex=6>')
print('								</td>')
print('							</tr>')
print('						</table>')
print('						<table class="table">')
print('							<thead>')
print('								<tr>')
print('									<th>Macro Nutrients</th>')
print('									<th style="text-align: right">Amount</th>')
print('									<th></th>')
print('									<th>Vitamins</th>')
print('									<th style="text-align: right">Amount</th>')
print('									<th></th>')
print('									<th>Minerals</th>')
print('									<th style="text-align: right">Amount</th>')
print('									<th></th>')
print('								</tr>')
print('							</thead>')
print('							<tbody>')

for x in range(15):
	print('								<tr>')

	if x < 11:
		print('									<td>%s</td>' % (key[x][0]))
		print('									<td style="text-align: right"><input type="text" name="%s" size="5" tabindex=%i></td>' % (key[x][0].lower().replace(' ', '-'), x + 7))
		print('									<td style="text-align: left">%s</td>' % (key[x][1]))
	else:
		print('									<td></td>')
		print('									<td></td>')
		print('									<td></td>')

	if x < 12:
		print('									<td>%s</td>' % (key[x + 11][0]))
		print('									<td style="text-align: right"><input type="text" name="%s" size="5" tabindex=%i></td>' % (key[x + 11][0].lower().replace(' ', '-'), x + 18))
		print('									<td style="text-align: left">%s</td>' % (key[x + 11][1]))
	else:
		print('									<td></td>')
		print('									<td></td>')
		print('									<td></td>')

	print('									<td>%s</td>' % (key[x + 24][0]))
	print('									<td style="text-align: right"><input type="text" name="%s" size="5" tabindex=%i></td>' % (key[x + 24][0].lower().replace(' ', '-'), x + 31))
	print('									<td style="text-align: left">%s</td>' % (key[x + 24][1]))
	print('								</tr>')

print('							</tbody>')
print('						</table>')
print('					</div>')
print('					<div class="modal-footer">')
print('						<input type="submit" class="btn btn-primary" value="Submit" tabindex=46>')
print('						<button type="button" class="btn btn-default" data-dismiss="modal" tabindex=47>Close</button>')
print('					</div>')
print('				</div>')
print('			</div>')
print('		</div>')
print('	</form>')

for ingredient in ingredients:
	print('	<div class="modal fade" id="%s" role="dialog">' % (ingredient[0].lower().replace(' ', '-')))
	print('		<div class="modal-dialog" style="width: 90%">')
	print('			<div class="modal-content">')
	print('				<div class="modal-header">')
	print('					<button type="button" class="close" data-dismiss="modal">&times;</button>')
	print('					<h4 class="modal-title">%s</h4>' % (ingredient[0]))
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
			print('								<td style="text-align: right">%.1f%s</td>' % (ingredient[x + 1], key[x][1]))
		else:
			print('								<td></td>')
			print('								<td></td>')

		print('								<td></td>')

		if x < 12:
			print('								<td>%s</td>' % (key[x + 11][0]))
			print('								<td style="text-align: right">%.1f%s</td>' % (ingredient[x + 12], key[x + 11][1]))
		else:
			print('								<td></td>')
			print('								<td></td>')

		print('								<td></td>')
		print('								<td>%s</td>' % (key[x + 24][0]))
		print('								<td style="text-align: right">%.1f%s</td>' % (ingredient[x + 25], key[x + 24][1]))
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
