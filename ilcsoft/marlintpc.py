##################################################
#
# MarlinTPC module
#
# Author: Peter Wienemann, University of Bonn
# Date: November 2007
#
##################################################

# custom imports
from marlinpkg import MarlinPKG
from util import *

class MarlinTPC(MarlinPKG):
    """ Responsible for the MarlinTPC installation process. """
    
    def __init__(self, userInput):
        MarlinPKG.__init__(self, "MarlinTPC", userInput)

        self.reqfiles = [["lib/libMarlinTPCReconstruction.a", "lib/libMarlinTPCReconstruction.so", "lib/libMarlinTPCReconstruction.dylib"],
                        [ "lib/libtpcconddata.a", "lib/libtpcconddata.so", "lib/libtpcconddata.dylib"]]

        self.reqmodules = [ "LCIO", "GEAR", "GSL", "Marlin", "LCCD", "ROOT", "AIDA", "CLHEP" ]
        #self.optmodules = [ "Mokka" ]

    def setMode(self, mode):
        MarlinPKG.setMode(self, mode)
        
        self.download.project = 'marlintpc'
        self.download.root = ''

    def postCheckDeps(self):
        MarlinPKG.postCheckDeps(self)

        self.envpath["PATH"].append( self.installPath+'/bin' )

