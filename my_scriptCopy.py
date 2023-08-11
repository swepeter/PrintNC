#!/usr/bin/env python
# -*- coding: utf-8 -*-
import linuxcnc
s = linuxcnc.stat()
s.poll()
# to find the loaded tool information it is in tool table index 0
if s.tool_table[0].id != 0: # a tool is loaded
    print s.spindle[0]["override_enabled"]
    
else:
    print "no tool loaded"