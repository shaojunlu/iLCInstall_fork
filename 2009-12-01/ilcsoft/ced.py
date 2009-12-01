##################################################
#
# CED module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################

# custom imports
from baseilc import BaseILC
from util import *


class CED(BaseILC):
    """ Responsible for the CED software installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "CED", "CED")

        self.reqfiles = [ ["lib/libCED.so","lib/libCED.a","lib/libCED.dylib"] ]

        self.download.root = "marlinreco"

        self.envcmake['CED_SERVER']='OFF'

    def compile(self):
        """ compile CED """
        
        os.chdir( self.installPath+'/build' )

        if( self.rebuild ):
            tryunlink( "CMakeCache.txt" )
        
        if( os.system( "cmake " + self.genCMakeCmd() + " .. 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )
        
        if( os.system( "make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )
        
        if( os.system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)
        self.envpath["PATH"].append( self.installPath + '/bin' )

        if( self.mode == "install" and self.envcmake.has_key("CED_SERVER") ):
            if( str(self.envcmake["CED_SERVER"]) == "1" or self.envcmake["CED_SERVER"] == "ON" ):
                # FIXME: MAC
                if( not os.path.exists( "/usr/include/GL/glut.h" ) and not os.path.exists( "/usr/include/glut.h" ) ):
                    print "glut-devel not found in your system!! you can get it from:\n[ http://freeglut.sourceforge.net/ ]"
                    print "CED_SERVER forced to OFF"
                    self.envcmake["CED_SERVER"] = "OFF"

