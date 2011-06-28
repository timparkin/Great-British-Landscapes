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

row = Template(open('row.template').read())
data = yaml.load(data_yaml)

early = "05:50"
late = "20:50"


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
   for t,v in [(early,'¹'),(late,'²')]:
       fullurl = u'http://www.landscapegb.com'+url
       print fullurl
       bitlyurl = str(api.shorten(fullurl))
       #bitlyurl = 'http://www.bit.ly/foo'
       print bitlyurl
       out.append( row.substitute( date=d.strftime('%d/%m/%Y'), time=t, message=text, url=bitlyurl, issue=issue, v=v) )
   d += delta

print ''.join(out)
print d.strftime('%d/%m/%Y')
