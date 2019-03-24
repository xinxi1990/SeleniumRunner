#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
from sr.client import main_run

cmd = sys.argv.pop(1)

if cmd in ["sr"]:
    main_run()

else:
   print("Miss debugging type.", "RED")

