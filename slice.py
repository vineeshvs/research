# Slicing code
# Courtesy: Stackoverflow and many other sites  

from glob import iglob
import shutil
import os
import sys

#----------------------------------------------------------------------
# Fresh execution of program

print "\nFresh execution of program" 
print "****************************\n"

#----------------------------------------------------------------------
# Function definitions

# Find a string between two strings
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        print "error"
        return ""

'''
# Testing function find_between
s = "123vineeshabc"
a = find_between( s, "123", "abc" )
print a
''' 
#----------------------------------------------------------------------
# Print the contents of a file

def print_file(file_name):
    f_1 = open (file_name)
    for line in f_1:
        print line    
    print "------------------------------------------------------------"

#----------------------------------------------------------------------
# Remove spaces in a list of strings

def rem_space(list_name):
    while True:
        try:
            list_name.remove("")
        except ValueError:
            print "No blank space in the string"
            break
        pass
#----------------------------------------------------------------------

'''
if 'Instructions' in open('full_adder.v').read():
    print "True"
else:
    print "False"
'''
#----------------------------------------------------------------------

lines = open("full_adder.v", 'rt').read()

#----------------------------------------------------------------------
# Junk

'''
first, second, rest = lines.split('Instructions',3)
open("output1.txt", 'wt').writelines(first)
open("output2.txt", 'wt').writelines(second)
open("output3.txt", 'wt').writelines(rest)
'''

'''
# Concatenation of two sections
destination=open("output4.txt",'wb')
shutil.copyfileobj(open("output1.txt",'rb'), destination)
shutil.copyfileobj(open("output3.txt",'rb'), destination)
destination.close()
'''

'''
#
fh=open("full_adder.v",'r')
for i in range(100):
    print fh.readline()
'''

#----------------------------------------------------------------------
# Calculating the total number of slices (num_slices)

num_slices = 0
for item in lines.split("\n"):
    if "// slice" in item:
        # print item.strip()
        num_slices += 1
'''

#----------------------------------------------------------------------
# Junk

# Split files
first, second, rest = lines.split('Instructions',num_slices+1)
open("output1.txt", 'wt').writelines(first)
open("output2.txt", 'wt').writelines(second)
open("output3.txt", 'wt').writelines(rest)

# Combine files
destination=open("output4.txt",'wb')
shutil.copyfileobj(open("output1.txt",'rb'), destination)
shutil.copyfileobj(open("output3.txt",'rb'), destination)
destination.close()
'''

#----------------------------------------------------------------------
# Creating slices

print "\nCreating slices"
print "**************\n"
for i in range(1, num_slices + 1):
    slice_i = lines.split("// slice", num_slices)[i]
    open("%d.txt" %(i),'wt').writelines(slice_i)
    # print_file ("%d.txt" %(i))

# ---------------------------------------------------------------------
# Searching for module name
 
# module = sys.stdin.readline()
module = raw_input ("Give the name of the module to be tested:")

print "Searching for module and doing concatenation "
# destination = open("combined_file.txt",'w')

'''
# Simple search of module and concatenation of slices
for i in xrange (1, num_slices + 1):
    if module in open('%d.txt' %(i)).read():
        print "True in %d.txt" %(i)
        # shutil.copyfileobj(open("%d.txt" %(i),'rb'), destination)
        with open("%d.txt" %(i)) as infile:
            destination.write (infile.read())
    elif "default_slice" in open('%d.txt' %(i)).read():
        with open("%d.txt" %(i)) as infile:
            destination.write (infile.read())
    else:
        print "False in %d.txt" %(i)
'''

# ---------------------------------------------------------------------
#Finding out the instructions related to the module specified

print "\nFinding out the instructions related to the module specified"
print "*************************************************************\n"
full_instruction_list = ['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7']
selected_instruction_set = []
for i in xrange (1, num_slices + 1):
    if module in open('%d.txt' %(i)).read():
        print "your module is found in %d.txt" %(i)
        for I in full_instruction_list:
            if I in open('%d.txt' %(i)).read():
                print "%s found in %d.txt" %(I, i)
                selected_instruction_set.append(I)

# To accommodate for default sections of slice
# Essential part of verilog code
selected_instruction_set.append('default_slice')

#----------------------------------------------------------------------
# Checking for slices which contain elements in selected_instruction_set and combining them

print "\nJoining slices"
print "**************\n"
destination = open("combined_file.txt",'w')
for i in xrange (1, num_slices + 1):
    for I in selected_instruction_set:
        # The line below will make sure that the test module is not included in the combined_file.txt file, but only the slices which have connection with the test module will be included in it
        if ((I in open('%d.txt' %(i)).read()) and (not (module in open('%d.txt' %(i)).read()))):
            print "True in %d.txt" %(i)
            with open("%d.txt" %(i)) as infile:
                destination.write (infile.read())
                break

destination.close()

# Check if the combined_file.txt is correct
print "printing combined_file.txt"
print_file("combined_file.txt")







#----------------------------------------------------------------------
#Extracting inputs and outputs of module to be tested

print "\nExtracting inputs and outputs of module to be tested"
print "****************************************************\n"
inputs_test_module = []
outputs_test_module = []
k = 0
for i in xrange (1, num_slices + 1):
    if module in open('%d.txt' %(i)).read():
        with open('%d.txt' %(i)) as f:
            print "test1"
            for line in f:
                if "Inputs" in line:
                    k = 1
                elif "Outputs" in line:
                    k = 2
                while k == 1:
                    inputs_test_module.append (find_between (line, "(", ")"))
                    if "End of inputs" in line:
                        k = 0
                    break
                while k == 2:
                    outputs_test_module.append (find_between (line, "(", ")"))
                    if "End of outputs" in line:
                        k = 0
                    break

'''
# There are spaces in the strings 'inputs_test_module' and 'outputs_test_module
print "inputs_test_module:"
print inputs_test_module
print "outputs_test_module:"
print outputs_test_module
'''
# -----------------------------------------------------------------------------

# Removing spaces in the strings 'inputs_test_module' and 'outputs_test_module
rem_space (inputs_test_module)
print inputs_test_module
rem_space (outputs_test_module)
print outputs_test_module

# -----------------------------------------------------------------------------

# Ignore this section. I don't know why I wrote this section. Let's figure out later 
# Checking for entries if inputs_test_module in the sliced section without MUT

'''
count = 0
lines_slice = open("combined_file.txt", 'r').read()

for i in inputs_test_module:
print i
'''

'''
count = count + 1
if "(" + i + ")":
print "(%s) found at line %d" %(i,count) 
break
'''     

#----------------------------------------------------------------------
'''
flist = open("combined_file.txt").readlines()

parsing = False
for line in flist:
    print line
    if line.startswith("\****t// Inputs"):
        parsing = True
    if line.startswith("\****t// End of inputs"):
        parsing = False
    if parsing:
        print line
'''
