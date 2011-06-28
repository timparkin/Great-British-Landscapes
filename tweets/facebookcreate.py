#! encoding=utf8
import bitly
from datetime import date 
from datetime import timedelta
from string import Template
import yaml
import sys

apikey = 'R_f5236a661a48b7a79555db4461d9aa9a'
api = bitly.Api(login='timparkin', apikey=apikey)

delta = timedelta(days=1)

data_filename = sys.argv[1]
data_yaml = open(data_filename).read()

row = Template(open('facebookrow.template').read())
data = yaml.load(data_yaml)


startdate = data['date']
issue = data['issue']
messages = data['messages']

print startdate
d,m,y = [int(d) for d in startdate.split('/')]
d = date( y,m,d )
out = []
for message in messages:
   url = message['url']
   text = message['text']
   fullurl = u'http://www.landscapegb.com'+url
   bitlyurl = str(api.shorten(fullurl))
   out.append( row.substitute( date=d.strftime('%d/%m/%Y'), time='05:50', message=text, url=bitlyurl, issue=issue) )
   d += delta

print ''.join(out)
