#!/usr/bin/env python
"""
This is a long, multiline description for a script that does nothing
"""

#-------------------------------------------------------------------------------
#--- Add other modules to the sys.path
#--- Will probably have to be done for the code which is using this API
#-------------------------------------------------------------------------------
import sys
import os.path
#sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

#-------------------------------------------------------------------------------
#--- IMPORTS (standard, then third party, then my own modules)
#-------------------------------------------------------------------------------
import argparse  #to read command line arguments

#-------------------------------------------------------------------------------
#--- HEADER
#-------------------------------------------------------------------------------
__author__ = "Miguel Riem de Oliveira"
__date__ = "2018"
__copyright__ = "LARDEMUA"
__credits__ = ["Miguel Riem de Oliveira"]
__license__ = "GNU Lesser General Public License v3.0"
__maintainer__ = __author__
__email__ = "mriem@ua.pt"

#-------------------------------------------------------------------------------
#--- FUNCTIONS
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
#--- MAIN
#-------------------------------------------------------------------------------
if __name__ == "__main__":

    #---------------------------------------
    #--- Parse command line argument
    #---------------------------------------
    ap = argparse.ArgumentParser()
    ap.add_argument("-n", "--name", help = "name of the user", required=True, type=string)
    ap.add_argument("-v", "--value", help = "a very important value to do nothing with", default=1234.5, type=float)
    args = vars(ap.parse_args())

    #---------------------------------------
    #--- INITIALIZATION
    #---------------------------------------
    #nothing to be done

    
    #---------------------------------------
    #--- EXECUTION
    #---------------------------------------
    #Just print a nonsensical message
    print('Hi ' + args['name'] + '. Why are you giving me number ' + str(args['value']) + '? I will do nothing with it ...' )

