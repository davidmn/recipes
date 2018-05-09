#!/usr/bin/python

import sys, argparse, os

parser = argparse.ArgumentParser()

parser.add_argument('--name', help='The name of the recipe')
parser.add_argument('--type', help='The type if the recipe, is it main, breakfast, or dessert?')
parser.add_argument('--serves', help='How many does it server or make?')

args=parser.parse_args()

allowed_types = ["main","dessert","breakfast"]

if not args.name:
    print("ERROR: name is a required argument!")
    sys.exit(1)

if not args.type:
    print("ERROR: type is a required argument")
    sys.exit(1)

if not args.type in allowed_types:
    print("ERROR: invalid type \"{}\"".format(args.type))
    sys.exit(1)

templatePath = 'template.md'
newFileName = args.name.lower().replace(' ', '-') + '.md'
outputPath = args.type + "/" + newFileName

if os.path.isfile(outputPath):
    print("ERROR: file {} already exists".format(outputPath))
    sys.exit(1)

with open(templatePath) as file :
  fileData = file.read()

fileData = fileData.replace('$name', args.name)
fileData = fileData.replace('$serves', args.serves)

with open(outputPath, 'w+') as file:
  file.write(fileData)

print("Created file " + outputPath)
