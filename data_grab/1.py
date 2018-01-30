# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 21:11:46 2018

@author: zylzlh
"""

import sys, re
regex=sys.argv[1]
for line in sys.stdin:
    if re.search(regex,line):
        sys.stdout.write(line)
