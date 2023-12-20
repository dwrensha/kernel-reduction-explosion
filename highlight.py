import argparse
import json

from pygments import highlight
from pygments.lexers import LeanLexer
from pygments.formatters import HtmlFormatter

parser = argparse.ArgumentParser(description="highlight traces")
parser.add_argument("input")

args = parser.parse_args()

FILE_PATH = args.input

with open(FILE_PATH, 'r') as file:
    data = json.load(file)

lexer = LeanLexer()
formatter = HtmlFormatter()

new_data = {}

for k in data.keys():
    new_array = []
    for l in data[k]:
        new_array.append(highlight(l, lexer, formatter))
    new_data[k] = new_array

print ("const data = {};".format(json.dumps(new_data)))
