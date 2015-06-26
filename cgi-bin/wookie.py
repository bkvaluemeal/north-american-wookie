#!/usr/bin/env python
from lib.wookie import Wookie
import sqlite3
import cgi

form = cgi.FieldStorage()
conn = sqlite3.connect('database.db')
c = conn.cursor()

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

if 'profile' not in form:
	print('	<form action="/cgi-bin/wookie.py" method="POST">')
	print('		<table class="table">')
	print('			<tbody>')
	print('				<tr>')
	print('					<td>Profile</td>')
	print('					<td>')
	print('						<select name="profile">')

	for row in c.execute('SELECT name FROM profiles'):
		print('							<option value="%s">%s</option>' % (row[0], row[0]))

	print('						</select>')
	print('					</td>')
	print('					<td>')
	print('						<p>Choose a profile</p>')
	print('					</td>')
	print('				</tr>')
	print('				<tr>')
	print('					<td></td>')
	print('					<td><input type="submit" value="Submit"></td>')
	print('					<td></td>')
	print('				</tr>')
	print('			</tbody>')
	print('		</table>')
	print('	</form>')
else:
	result = Wookie().getBest()

	print('	<table class="table">')
	print('		<thead>')
	print('			<tr>')
	print('				<th>Recipe</th>')
	print('			</tr>')
	print('		</thead>')
	print('		<tbody>')

	for item in result.getRecipe():
		print('			<tr>')
		print('				<td>%s</td>' % (item))
		print('			</tr>')

	print('		</tbody>')
	print('	</table>')
	print('	<h2 style="text-align: center; padding: 1em">$%.2f per day</h2>' % (result.getPrice()))

print('	<div class="row">')
print('		<footer style="text-align: center">')
print('			<p>Copyright 2015 Justin Willis</p>')
print('			<a href="https://github.com/bkvaluemeal/north-american-wookie" class="btn btn-link" role="button">GitHub</a>')
print('		</footer>')
print('	</div>')
print('</div>')
print('</body>')
print('</html>')
