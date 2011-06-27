

from string import Template
import yaml
import sys

data_filename = sys.argv[1]
data_yaml = open(data_filename).read()

index = Template(open('video.template').read())

datas = yaml.load(data_yaml)

for data in datas:
    out = index.substitute( PART=data['part'],
                            issue = data['issue'],
                           awsdir = data['awsdir'],
                           suffix=data['suffix'],
                           filename = data['filename'],
                           mediaid2500 = data['mediaid2500'],
                           mediaid1000 = data['mediaid1000'],
                           staticdir = data['staticdir']
                          )

    print out



data_filename = sys.argv[1]
data_yaml = open(data_filename).read()

index = Template(open('upload.txt').read())

datas = yaml.load(data_yaml)

for data in datas:
    out = index.substitute( PART=data['part'],
                            issue = data['issue'],
                           awsdir = data['awsdir'],
                           suffix=data['suffix'],
                           filename = data['filename'],
                           mediaid2500 = data['mediaid2500'],
                           mediaid1000 = data['mediaid1000'],
                           staticdir = data['staticdir']
                          )

    print out

