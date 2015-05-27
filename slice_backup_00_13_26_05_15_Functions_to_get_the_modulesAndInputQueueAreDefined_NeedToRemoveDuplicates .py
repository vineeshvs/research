# Slicing code
# Courtesy: Stackoverflow and many other sites  

from glob import iglob
import shutil
import os
import sys

print "\nHere we go" 
print "*************\n"

""" FUNCTION DEFINITIONS """
############################

"""Find a string between two strings"""
def find_between(s, first, last):
    try:
        start = s.index(first)+ len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        #print "error"
        return ""

'''
# Testing function find_between
s = "123vineeshabc"
a = find_between(s, "123", "abc")
print a
''' 

"""Print the contents of a file"""
def print_file(file_name):
    f_1 = open (file_name)
    for line in f_1:
        print line    

'''Remove spaces in a list of strings'''
def rem_space(list_name):  
	while True:
		try:
			list_name.remove("")
		except ValueError:
		    #print "No blank space in the string"
		    break
		pass

""" Find out the modules which gives certain signals as output """
def locate_modules(verilog_file, output_signal):
    	lines = open(verilog_file, 'rt').read()
	modules = []
	k=0
	i=0			
        l=0
	with open('full_adder.v')as f:
            for line in f:
                if i==1:
                    """Inside the module instantiation"""    
                    m=line.split()[1]
                    #print "The module name is %s" %(m)
                    #print "output_signal is %s" %(output_signal)
                    i=0
                    k=1
                    #modules.append(line.split()[1])
                    #print ("inside module")
                if k==1:
                    #print "k==1"
                    """Extracting the module name"""
                    if l==1:
                        #print "l==1"
                        print find_between(line,"(",")")
                        if(find_between(line,"(",")")==output_signal):
                            #rem_space(modules.append(m))
                            modules.append(m)
                            print"The module list %s" %(modules)
                            i=0
                            k=0
                    elif "End of outputs" in line:
                        #print "End of outputs"
                        l=0
                        k=0
                        #print "l=0"
                    elif "Outputs" in line:
                        l=1 
                        #print "Outputs detected"
                    else:
                        #print"Neither outputs not End of outputs"  
                        #print line
                        l=0
                        k=1
                if "Module instantiation" in line:
                    i = 1
                    k=0
                    l=0
                    #print "Module instantiation"
                elif ");" in line:
                    i = 0
                    k=0
                    l=0
                    #print "Module ends" 
        return modules

"""Function to return the inputs and outputs of a module
Inputs: The name of MUT (Add the verilog file name later)
Outputs: Two lists inputs_test_module and outputs_test_module"""
def find_inputs_of_module(verilog_file, module_name):
	lines = open(verilog_file, 'rt').read()
	""" Extracting inputs and outputs of module to be tested """
	inputs_test_module = []
	outputs_test_module = []
	k = 0
	i = 0		
	with open('full_adder.v')as f:
		for line in f:
			if module_name in line:
				i = 1
			elif ");" in line:
				i = 0
			if i == 1:
				if "Inputs" in line:
					k = 1
				elif "Outputs" in line:
					k = 2
				if k == 1:	
					#m = find_between (line, "(", ")")
					#print m
					inputs_test_module.append (find_between (line, "(", ")"))
					if "End of inputs" in line:
						k = 0
				elif k == 2:	
					#m = find_between (line, "(", ")")
					#print m
					outputs_test_module.append (find_between (line, "(", ")"))
					if "End of outputs" in line:
						k = 0
	""" Removing spaces in the strings 'inputs_test_module' and 'outputs_test_module """
	rem_space (inputs_test_module)
	#print inputs_test_module
	rem_space (outputs_test_module)
	#print outputs_test_module
	return inputs_test_module, outputs_test_module



""" MAIN()"""
##############

module = raw_input ("Give the name of the module to be tested:")
"""Get the inputs and outputs of the MUT"""
print find_inputs_of_module("full_adder.v", module)
inputs_test_module,outputs_test_module=find_inputs_of_module("full_adder.v", module)

#locate_modules("full_adder.v","s3")
modules=locate_modules("full_adder.v",inputs_test_module[0])
print modules
