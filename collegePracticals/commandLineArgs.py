# TASK : count the no of arguments from command line


import sys

def getCmdLineArgsCount():
    args = len(sys.argv)
    args = args - 1   # because argumets are stated form file name we are ignoring file name
    return args


print(getCmdLineArgsCount())