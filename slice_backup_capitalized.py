# Slicing code
# Courtesy: Stackoverflow and many other sites  

from glob import iglob
import shutil
import os
import sys

#------------------------- Function definitions------------------------

# Find a string between two strings
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        print "error"
        return ""

_
# Testing function find_between
a = find_between( s, "123", "abc" )
print a
''' 

# PRINT THE CONTENTS OF A FILE
DEF PRINT_FILE(FILE_NAME):
    F_1 = OPEN (FILE_NAME)
    FOR LINE IN F_1:
        PRINT LINE    
    PRINT "------------------------------------------------"

#----------------------------------------------------------------------

'''
IF 'INSTRUCTIONS' IN OPEN('FULL_ADDER.V').READ():
    PRINT "TRUE"
ELSE:
    PRINT "FALSE"
'''

LINES = OPEN("FULL_ADDER.V", 'RT').READ()

'''
FIRST, SECOND, REST = LINES.SPLIT('INSTRUCTIONS',3)
OPEN("OUTPUT1.TXT", 'WT').WRITELINES(FIRST)
OPEN("OUTPUT2.TXT", 'WT').WRITELINES(SECOND)
OPEN("OUTPUT3.TXT", 'WT').WRITELINES(REST)
'''

'''
# CONCATENATION OF TWO SECTIONS
DESTINATION=OPEN("OUTPUT4.TXT",'WB')
SHUTIL.COPYFILEOBJ(OPEN("OUTPUT1.TXT",'RB'), DESTINATION)
SHUTIL.COPYFILEOBJ(OPEN("OUTPUT3.TXT",'RB'), DESTINATION)
DESTINATION.CLOSE()
'''

'''
#
FH=OPEN("FULL_ADDER.V",'R')
FOR I IN RANGE(100):
    PRINT FH.READLINE()
'''

#
NUM_SLICES = 0
FOR ITEM IN LINES.SPLIT("\N"):
    IF "// SLICE" IN ITEM:
        PRINT ITEM.STRIP()
        NUM_SLICES += 1
'''

# SPLIT FILES
FIRST, SECOND, REST = LINES.SPLIT('INSTRUCTIONS',NUM_SLICES+1)
OPEN("OUTPUT1.TXT", 'WT').WRITELINES(FIRST)
OPEN("OUTPUT2.TXT", 'WT').WRITELINES(SECOND)
OPEN("OUTPUT3.TXT", 'WT').WRITELINES(REST)

# COMBINE FILES
DESTINATION=OPEN("OUTPUT4.TXT",'WB')
SHUTIL.COPYFILEOBJ(OPEN("OUTPUT1.TXT",'RB'), DESTINATION)
SHUTIL.COPYFILEOBJ(OPEN("OUTPUT3.TXT",'RB'), DESTINATION)
DESTINATION.CLOSE()
'''

# CREATING SLICES
FOR I IN RANGE(1, NUM_SLICES + 1):
    SLICE_I = LINES.SPLIT("// SLICE", NUM_SLICES)[I]
    OPEN("%D.TXT" %(I),'WT').WRITELINES(SLICE_I)
    PRINT_FILE ("%D.TXT" %(I))


# ---------------------------------------------------------------------
# SEARCHING FOR MODULE NAME
 
# MODULE = SYS.STDIN.READLINE()
MODULE = RAW_INPUT ("GIVE THE NAME OF THE MODULE TO BE TESTED:")

'''
IF MODULE == "STOP":
    PRINT 'STOP DETECTED'
ELSE:
PRINT 'NO STOP DETECTED'
'''

PRINT "SEARCHING FOR MODULE AND DOING CONCATENATION "
# DESTINATION = OPEN("COMBINED_FILE.TXT",'W')

'''
# SIMPLE SEARCH OF MODULE AND CONCATENATION OF SLICES
FOR I IN XRANGE (1, NUM_SLICES + 1):
    IF MODULE IN OPEN('%D.TXT' %(I)).READ():
        PRINT "TRUE IN %D.TXT" %(I)
        # SHUTIL.COPYFILEOBJ(OPEN("%D.TXT" %(I),'RB'), DESTINATION)
        WITH OPEN("%D.TXT" %(I)) AS INFILE:
            DESTINATION.WRITE (INFILE.READ())
    ELIF "DEFAULT_SLICE" IN OPEN('%D.TXT' %(I)).READ():
        WITH OPEN("%D.TXT" %(I)) AS INFILE:
            DESTINATION.WRITE (INFILE.READ())
    ELSE:
        PRINT "FALSE IN %D.TXT" %(I)
'''

# ------------FINDING OUT THE INSTRUCTIONS RELATED TO THE MODULE SPECIFIED---------
FULL_INSTRUCTION_LIST = ['I1', 'I2', 'I3', 'I4', 'I5']
SELECTED_INSTRUCTION_SET = []
FOR I IN XRANGE (1, NUM_SLICES + 1):
    IF MODULE IN OPEN('%D.TXT' %(I)).READ():
        PRINT "YOUR MODULE IS FOUND IN %D.TXT" %(I)
        FOR I IN FULL_INSTRUCTION_LIST:
            IF I IN OPEN('%D.TXT' %(I)).READ():
                PRINT "%S FOUND IN %D.TXT" %(I, I)
                SELECTED_INSTRUCTION_SET.APPEND(I)

# TO ACCOMMODATE FOR DEFAULT SECTIONS OF SLICE
# ESSENTIAL PART OF VERILOG CODE
SELECTED_INSTRUCTION_SET.APPEND('DEFAULT_SLICE')

# ------CHECKING FOR SLICES WHICH CONTAIN ELEMENTS IN SELECTED_INSTRUCTION_SET------
# AND COMBINING THEM
PRINT "------------------------JOINING SLICES---------------------------------------"
DESTINATION = OPEN("COMBINED_FILE.TXT",'W')
FOR I IN XRANGE (1, NUM_SLICES + 1):
    FOR I IN SELECTED_INSTRUCTION_SET:
        IF I IN OPEN('%D.TXT' %(I)).READ():
            #PRINT "TRUE IN %D.TXT" %(I)
            WITH OPEN("%D.TXT" %(I)) AS INFILE:
                DESTINATION.WRITE (INFILE.READ())
                BREAK

DESTINATION.CLOSE()

# PRINT "PRINTING COMBINED_FILE.TXT"
# PRINT_FILE("COMBINED_FILE.TXT")

#---------------EXTRACTING INPUTS AND OUTPUTS OF MODULE TO BE TESTED--------------------"
INPUTS_TEST_MODULE = []
OUTPUTS_TEST_MODULE = []
K = 1
FOR I IN XRANGE (1, NUM_SLICES + 1):
    IF MODULE IN OPEN('%D.TXT' %(I)).READ():
        WITH OPEN('%D.TXT' %(I)) AS F:
            PRINT "TEST1"
            FOR LINE IN F:
                IF "INPUTS" IN LINE:
                    PRINT "\\\ INPUTS FOUND"
                    INPUTS_TEST_MODULE = FIND_Between (line, "(", ")")
                    print inputs_test_module
                    # k = k + 1
                    # inputs_test_module.append(b)
                    # print inputs_test_module.join (b)
                    # inputs_test_module + b
                    # inputs_test_module.append("test")
                elif "End of inputs" in line:
                    print "\\\ End of inputs found"
                if "Outputs" in line:
                    print "\\\ Outputs found"
                    outputs_test_module.append(find_between (line, "(", ")"))
                elif "End of outputs" in line:
                    print "\\\ End of outputs found"

print "inputs_test_module:"
print inputs_test_module
print "outputs_test_module:"
print outputs_test_module

