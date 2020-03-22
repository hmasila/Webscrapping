import re
import json
import mechanize
import lxml.html

br = mechanize.Browser()
br.open("https://andela-online-store.herokuapp.com/")

br.follow_link(text_regex=r"(?i)join")

fields = dict(
	username='arusha',
	password='arusha',
	password_confirmation='arusha',
	phone='23456789',
	last_name='farm',
	first_name='shamba')

br.form = list(br.forms())[0]

for field, value in fields.items():
  control = br.form.find_control(field)
  control.value = value

response = br.submit()

br.follow_link(text_regex=r"(?i)log")

fields = dict(
	username='arusha',
	password='arusha')

br.form = list(br.forms())[0]

for field, value in fields.items():
  control = br.form.find_control(field)
  control.value = value

br.submit()
