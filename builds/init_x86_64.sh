#!/bin/bash


if [ "$( cat /etc/*-release | grep Scientific )" ]; then
    OS=slc6
elif [ "$( cat /etc/*-release | grep CentOS )" ]; then
    OS=centos7
else
    echo "UNKNOWN OS"
    exit 1
fi


if [ -z ${GCC_VERSION} ]; then
    GCC_VERSION=4.8.5
fi
  
if [ -z ${BUILD_TYPE} ]; then
    BUILD_TYPE=opt
fi

GCC_VER=`echo ${GCC_VERSION} | sed -e 's/\.//g' | cut -c 1-2`

# General variables
CLICREPO=/cvmfs/clicdp.cern.ch
BUILD_FLAVOUR=x86_64-${OS}-gcc${GCC_VER}-${BUILD_TYPE}
#--------------------------------------------------------------------------------
#     GCC
#--------------------------------------------------------------------------------

source ${CLICREPO}/compilers/gcc/${GCC_VERSION}/x86_64-${OS}/setup.sh

#--------------------------------------------------------------------------------
#     CMake
#--------------------------------------------------------------------------------

export CMAKE_HOME=${CLICREPO}/software/CMake/3.5.2/${BUILD_FLAVOUR}
export PATH=${CMAKE_HOME}/bin:$PATH

#--------------------------------------------------------------------------------
#     Python
#--------------------------------------------------------------------------------

export PYTHONDIR=${CLICREPO}/software/Python/2.7.11/${BUILD_FLAVOUR}
export PATH=$PYTHONDIR/bin:$PATH
export LD_LIBRARY_PATH=$PYTHONDIR/lib:$LD_LIBRARY_PATH


