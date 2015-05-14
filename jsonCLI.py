#!/usr/bin/python3
'''
    A command line tool for JSON
    Copyright (C) 2015 Christoph "criztovyl" Schulz

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
import json
import sys
input=""
for line in sys.stdin:
    input = input + line.strip();
if( input == ""):
    input="{}"
json_data = json.loads(input)
args = sys.argv
args.pop(0)
action=""
if(len(args) > 0 and args[0] in ("inspect")):
    action = args.pop(0)
for arg in args:
    try:
        arg = int(arg)
    except:
        pass
    try:
        json_data = json_data[arg]
    except (IndexError, KeyError, TypeError) as e:
        print("%s: %s" % (type(e).__name__, e))
        sys.exit(1)
#print("JSON data:")
#print("Action:")
#print(action)
if(action == "inspect"):
    json_type=type(json_data)
    if(json_type is list):
        print("It's a list with length %i." % len(json_data))
    elif(json_type is dict):
        print("It's a dict with this keys: ")
        print(" ".join(json_data.keys()))
    else:
        print("Type %s" % json_type.__name__)
        print(json_data)
else:
    print(json.dumps(json_data, sort_keys=True, indent=4))
