#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
from src.cli import main_run

cmd = sys.argv.pop(1)

if cmd in ["src"]:
    main_run()

else:
   print("Miss debugging type.", "RED")

