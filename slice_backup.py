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
        return ""

'''
# Testing function find_between
a = find_between( s, "123", "abc" )
print a
''' 

# Print the contents of a file
def print_file(file_name):
    f_1 = open (file_name)
    for line in f_1:
        print line    
    print "------------------------------------------------"

#----------------------------------------------------------------------

'''
if 'Instructions' in open('full_adder.v').read():
    print "True"
else:
    print "False"
'''

lines = open("full_adder.v", 'rt').read()

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

#
num_slices = 0
for item in lines.split("\n"):
    if "// slice" in item:
        print item.strip()
        num_slices += 1
'''

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

# Creating slices
for i in range(1, num_slices + 1):
    slice_i = lines.split("// slice", num_slices)[i]
    open("%d.txt" %(i),'wt').writelines(slice_i)
    print_file ("%d.txt" %(i))


# ---------------------------------------------------------------------
# Searching for module name
 
# module = sys.stdin.readline()
module = raw_input ("Give the name of the module to be tested:")

'''
if module == "stop":
    print 'stop detected'
else:
print 'no stop detected'
'''

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

# ------------Finding out the instructions related to the module specified---------
full_instruction_list = ['I1', 'I2', 'I3', 'I4', 'I5']
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

# ------Checking for slices which contain elements in selected_instruction_set------
# And combining them
print "------------------------Joining slices---------------------------------------"
destination = open("combined_file.txt",'w')
for i in xrange (1, num_slices + 1):
    for I in selected_instruction_set:
        if I in open('%d.txt' %(i)).read():
            #print "True in %d.txt" %(i)
            with open("%d.txt" %(i)) as infile:
                destination.write (infile.read())
                break

destination.close()

# print "printing combined_file.txt"
# print_file("combined_file.txt")

#---------------Extracting inputs and outputs of module to be tested--------------------"
inputs_test_module = []
outputs_test_module = []
k = 1
for i in xrange (1, num_slices + 1):
    if module in open('%d.txt' %(i)).read():
        with open('%d.txt' %(i)) as f:
            print "test1"
            for line in f:
                if "Inputs" in line:
                    print "\\\ Inputs found"
                    inputs_test_module = find_between (line, "(", ")")
                    k = k + 1
                    # inputs_test_module.append(b)
                    print inputs_test_module.join (b)
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

