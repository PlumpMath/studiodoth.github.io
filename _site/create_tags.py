#!/usr/bin/env python

'''
tag_generator.py
Copyright 2017 Long Qian
Contact: lqian8@jhu.edu
This script creates tags for your Jekyll blog hosted by Github page.
No plugins required.
'''

import glob
import os
import json
from os import walk

post_dir = '_posts/'
tag_dir = 'tag/'

for file in os.listdir(tag_dir):
    file_path = os.path.join(post_dir, file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(e)

filenames = []
for (dirpath, dirnames, f) in walk(post_dir):
    filenames.extend(f)

total_tags = []
for filename in filenames:
    print(filename)
    f = open(post_dir+filename, 'r', encoding="utf8")
    crawl = False
    for line in f:
        if crawl:
            if line.startswith("tags: "):
                total_tags.extend(json.loads(line[6:]))
        if line.strip() == '---':
            if not crawl:
                crawl = True
            else:
                crawl = False
                break
    f.close()
total_tags = set(total_tags)

old_tags = glob.glob(tag_dir + '*.md')
for tag in old_tags:
    os.remove(tag)

for tag in total_tags:
    tag_filename = tag_dir + tag + '.md'
    f = open(tag_filename, 'a')
    write_str = '---\nlayout: tagpage\ntitle: \"Tag: ' + tag + '\"\ntag: ' + tag + '\nrobots: noindex\n---\n'
    f.write(write_str)
    f.close()
print("Tags generated, count", total_tags.__len__())