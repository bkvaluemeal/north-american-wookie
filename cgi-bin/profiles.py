#!/usr/bin/env python
from lib import label
import sqlite3
import cgi

form = cgi.FieldStorage()
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

def doForm():
	if 'action' in form:
		action = form.getvalue('action')
		stats = ()

		if action == 'add':
			try:
				stats += (form.getvalue('name'),)
			except:
				return 1

			for stat in key:
				try:
					stats += (float(form.getvalue(stat[0].lower().replace(' ', '-'))),)
				except:
					stats += (0,)

			c.execute("INSERT INTO profiles VALUES ('%s', %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f)" % stats)

			conn.commit()
		elif action == 'delete':
			c.execute("DELETE FROM profiles WHERE name = '%s'" % (form.getvalue('name')))

			conn.commit()
		elif action == 'edit':
			try:
				stats += (form.getvalue('name'),)
			except:
				return 1

			for stat in key:
				try:
					stats += (float(form.getvalue(stat[0].lower().replace(' ', '-'))),)
				except:
					stats += (0,)

			c.execute("DELETE FROM profiles WHERE name = '%s'" % (form.getvalue('original')))
			c.execute("INSERT INTO profiles VALUES ('%s', %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f)" % stats)

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

if error == 1:
	print('	<h2 style="color: red; text-align: center">Missing form data</h2>')

print('	<button type="button" class="btn btn-sm btn-success" style="margin-bottom: 2em" data-toggle="modal" data-target="#add">Add</button>')
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
print('	<form action="/cgi-bin/profiles.py" method="POST">')
print('		<input type="hidden" name="action" value="add">')
print('		<div id="add" class="modal fade" role="dialog">')
print('			<div class="modal-dialog" style="width: 90%">')
print('				<div class="modal-content">')
print('					<div class="modal-header">')
print('						<button type="button" class="close" data-dismiss="modal">&times;</button>')
print('						<h4 class="modal-title"><input type="text" name="name" placeholder="New Profile" tabindex=1></h4>')
print('					</div>')
print('					<div class="modal-body">')
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

for profile in profiles:
	print('	<form action="/cgi-bin/profiles.py" method="POST">')
	print('		<input type="hidden" name="action" value="edit">')
	print('		<input type="hidden" name="original" value="%s">' % (profile[0]))
	print('		<div id="%s-edit" class="modal fade" role="dialog">' % (profile[0].lower().replace(' ', '-')))
	print('			<div class="modal-dialog" style="width: 90%">')
	print('				<div class="modal-content">')
	print('					<div class="modal-header">')
	print('						<button type="button" class="close" data-dismiss="modal">&times;</button>')
	print('						<h4 class="modal-title"><input type="text" name="name" value="%s" tabindex=1></h4>' % (profile[0]))
	print('					</div>')
	print('					<div class="modal-body">')
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
			print('									<td style="text-align: right"><input type="text" name="%s" size="5" value="%.1f" tabindex=%i></td>' % (key[x][0].lower().replace(' ', '-'), profile[x + 1], x + 7))
			print('									<td style="text-align: left">%s</td>' % (key[x][1]))
		else:
			print('									<td></td>')
			print('									<td></td>')
			print('									<td></td>')

		if x < 12:
			print('									<td>%s</td>' % (key[x + 11][0]))
			print('									<td style="text-align: right"><input type="text" name="%s" size="5" value="%.1f" tabindex=%i></td>' % (key[x + 11][0].lower().replace(' ', '-'), profile[x + 12], x + 18))
			print('									<td style="text-align: left">%s</td>' % (key[x + 11][1]))
		else:
			print('									<td></td>')
			print('									<td></td>')
			print('									<td></td>')

		print('									<td>%s</td>' % (key[x + 24][0]))
		print('									<td style="text-align: right"><input type="text" name="%s" size="5" value="%.1f" tabindex=%i></td>' % (key[x + 24][0].lower().replace(' ', '-'), profile[x + 25], x + 31))
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
	print('				<form action="/cgi-bin/profiles.py" method="POST">')
	print('					<div class="modal-footer">')
	print('						<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#%s-edit" data-dismiss="modal">Edit</button>' % (profile[0].lower().replace(' ', '-')))
	print('						<input type="hidden" name="action" value="delete">')
	print('						<input type="hidden" name="name" value="%s">' % (profile[0]))
	print('						<input type="submit" class="btn btn-danger" value="Delete">')
	print('						<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>')
	print('					</div>')
	print('				</form>')
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
