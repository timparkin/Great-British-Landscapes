

from string import Template
import yaml
import sys

data_filename = sys.argv[1]
data_yaml = open(data_filename).read()

index = Template(open('before-after.template').read())
beforerow = Template(open('before-row.template').read())
afterrow = Template(open('after-row.template').read())

datas = yaml.load(data_yaml)

prefixjs = """
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js" type="text/javascript"></script>
<script src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.7.1/jquery-ui.min.js" type="text/javascript"></script>
<script src="http://static.timparkin.co.uk/static/landscapegb/1/shooting-into-the-sun/js/jquery.beforeafter.js"></script>
<script type="text/javascript">// <![CDATA[
$(function() {
"""
lines = []
for n,item in enumerate(datas):
    N = str(n+1)
    lines.append( "$('.beforeAfter" + N + "').beforeAfter();")

prefixjs += '\n'.join(lines)
prefixjs += """
$('.swapper').mousedown(function() {
    var base = $(this).parent().attr('urlbase');
    var img = $(this).attr('img');
    var target = $(this).attr('target');
    var title = $(this).text();
    var beforeafter = $(this).attr('beforeafter');
    $('.beforeAfter'+target+' '+beforeafter).attr('src',base+'/'+img);
    $('.beforeAfter'+target+'-desc'+' '+beforeafter).html(title);
});
    }
);
// ]]></script>
"""
print prefixjs


for n,data in enumerate(datas):
    N = str(n+1)
    brow = ''
    arow = ''
    if data['e6suffix'] is None:
        e6suffix = ''
    else:
        e6suffix = ' ' + data['e6suffix']
    if data['c41suffix'] is None:
        c41suffix = ''
    else:
        c41suffix = ' ' + data['c41suffix']
    for film in data['e6films']:
        b = beforerow.substitute( film=film, suffix = e6suffix ,N=N)
        a = afterrow.substitute( film=film, suffix = e6suffix,N=N )
        brow += b + '\n'
        arow += a + '\n'
    for film in data['c41films']:
        b = beforerow.substitute( film=film, suffix = c41suffix ,N=N)
        a = afterrow.substitute( film=film, suffix = c41suffix,N=N )
        brow += b + '\n'
        arow += a + '\n'
    out = index.substitute( title=data['title'],
                            directory = data['directory'],
                            issue = data['issue'],
                            N = N,
                            width = data['width'],
                            height = data['height'],
                            brow = brow,
                            arow = arow,
                            suffix=e6suffix,
                          )

    print out



