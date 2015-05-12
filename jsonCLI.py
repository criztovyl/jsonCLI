"""
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
"""
#!/usr/bin/python3
import json
import sys
input=""
for line in sys.stdin:
    input = input + line.strip();
json_data = json.loads(input)
args = sys.argv
args.pop(0)
for arg in args:
    try:
        arg = int(arg)
    except:
        pass
    json_data = json_data[arg]
print(json_data)
