#!/usr/bin/env python3
import sys
import pathlib
import lz4.block
import json
import socket

path = pathlib.Path.home().joinpath('.mozilla/firefox')
files = path.glob('*default*/sessionstore-backups/recovery.js*')
unique_list = []

for f in files:
    b = f.read_bytes()
    if b[:8] == b'mozLz40\0':
        b = lz4.block.decompress(b[8:])
    j = json.loads(b)
    for w in j['windows']:
        for t in w['tabs']:
            try:
                i = t['index'] - 1
            except:
                pass
            site = t['entries'][i]['url'].split('/')
            try:
                unique_list.append(socket.gethostbyname(site[2]))
            except IndexError:
                pass
unique_list = set(unique_list)
for i in unique_list:
    print(i)
print(len(unique_list),'unique IP')
