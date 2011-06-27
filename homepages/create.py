

from string import Template
import yaml
import sys

data_filename = sys.argv[1]
data_yaml = open(data_filename).read()

heroitem = Template(open('hero.template').read())
main = Template(open('main.template').read())
callout = Template(open('callout.template').read())
calloutsrow = Template(open('calloutsrow.template').read())

datas = yaml.load(data_yaml)

issue = datas['issue']
heros = datas['heros']
callouts = datas['callouts']

toprow = []
for n,data in enumerate(heros):

    nl = chr(97+n)
    img = 'http://static.timparkin.co.uk/static/landscapegb/%s/images/%s.jpg'%(issue,data['img'])
    hero = heroitem.substitute( n=n,nl=nl,title=data['title'],desc=data['desc'],img=img,link=data['link'],imgalt=data.get('imgalt',data['title']) )
    

    toprow.append(hero)

row = []
allrows = []
for n,data in enumerate(callouts):

    nl = chr(97+divmod(n,3)[1])
    img = 'http://static.timparkin.co.uk/static/landscapegb/%s/images/%s.jpg'%(issue,data['img'])
    calloutrow = callout.substitute( n=divmod(n,3)[1],nl=nl,title=data['title'],desc=data['desc'],img=img,link=data['link'],imgalt=data.get('imgalt',data['title']) )
    

    row.append(calloutrow)
    if divmod(n+1,3)[1] == 0:
        calloutsrowout = calloutsrow.substitute( callouts='\n'.join(row) )
        allrows.append(calloutsrowout)
        row = []

if len(row) != 0:
    if len(row) == 1:
        row.append('<div class="cfct-block block-1 cfct-block-b"></div>')
        row.append('<div class="cfct-block block-2 cfct-block-c"></div>')
    if len(row) == 2:
        row.append('<div class="cfct-block block-2 cfct-block-c"></div>')
    calloutsrowout = calloutsrow.substitute( callouts='\n'.join(row) )
    allrows.append(calloutsrowout)
out = main.substitute( heros='\n'.join(toprow), calloutrows='\n'.join(allrows) )
print out.replace('\n','')
#print out

