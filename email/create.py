

from string import Template
import yaml
import sys

data_filename = sys.argv[1]
data_yaml = open(data_filename).read()

email = Template(open('email.template').read())
data = yaml.load(data_yaml)


ntextarray = {
16: 'Sixteen',
17: 'Seventeen',
18: 'Eighteen',
19: 'Nineteen',
20: 'Twenty',
21: 'Twenty One',
22: 'Twenty Two',
23: 'Twenty Three',
24: 'Twenty Four',
}




nn = data['nn']
content = data['content']
ntext = ntextarray[int(nn)]
nextn = int(24 - (nn/2))
content = '<p>%s</p>'%'</p><p>'.join(line for line in content.splitlines() if line.strip() != '')

out = email.substitute( nn=nn, content=content, nextn=nextn, ntext=ntext )

print out

