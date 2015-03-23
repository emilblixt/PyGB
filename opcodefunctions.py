#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      EM007
#
# Created:     11-02-2015
# Copyright:   (c) EM007 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def LD():
    print "LD"
    print self.Register["A"]

def NOP():
    print "NOP"


Cycles = [57, 3]
OpCodes = [
    NOP, LD, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    ]