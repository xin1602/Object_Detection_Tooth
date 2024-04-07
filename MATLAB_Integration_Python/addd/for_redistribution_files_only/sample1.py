#!/usr/bin/env python
"""
Sample script that uses the addd module created using MATLAB Compiler SDK.
Refer to the MATLAB Compiler SDK documentation for more information.
"""
from __future__ import print_function
import addd
import matlab
my_addd = addd.initialize()
xIn=  matlab.double([5.0], size=(1, 1))
yIn=  matlab.double([6.0], size=(1, 1))
zOut=  my_addd.addd(xIn, yIn)
print (zOut, sep='\n')
my_addd.terminate()