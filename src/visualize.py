#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    print(k,':',v)

print(items)
keys = [tup[0] for tup in items][0:10]
values = [v[1] for v in items][0:10]

# plot bar graph
plt.bar(range(len(keys)), values)
plt.xticks(range(len(keys)), keys)
print("key:", keys)
print("values:", values)

# set title and axis 
if args.input_path[-1] == "g":
    plt.xlabel("Language")
else:
    plt.xlabel("Country")
if args.percent:
    plt.ylabel("percent of total tweet")
else:
    plt.ylabel("number of tweets")

# save bar graph as PNG file
if args.input_path[-1] == 'g':
    plt.savefig(args.key[1:] + '2_lang.png')
else:
    plt.savefig(args.key[1:] + '2_country.png')
