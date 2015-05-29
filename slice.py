# Slicing code
# Courtesy: Stackoverflow and many other sites  

import shutil
import os
import sys
import re
import logging
"""Importing the constants defined in the file constants.py"""
from constants import *
from glob import iglob

print "\nHere we go" 
print "*************\n"

""" FUNCTION DEFINITIONS """
############################

def find_between(s, first, last):
    """Find a string between two strings"""
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

def print_file(file_name):
    """Print the contents of a file"""
    f_1 = open (file_name)
    for line in f_1:
        print line    

def rem_space(list_name):  
    '''Remove spaces in a list of strings'''
    while True:
        try:
            list_name.remove("")
        except ValueError:
		    #print "No blank space in the string"
            break
        pass

def locate_modules(verilog_file, output_signal):
    """ Find out the modules which gives certain signals as output """
    lines = open(verilog_file, 'rt').read()
    module=""
    k=0
    i=0			
    l=0
    with open(verilog_file)as f:
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
                        #print find_between(line,"(",")")
                    if(find_between(line,"(",")")==output_signal):
                            #rem_space(modules.append(m))
                        module=m
                            #print"The module list %s" %(module)
                        i=0
                        k=0
                elif "End of outputs" in line:
                        #print "End of outputs"
                    l=0
                    k=0
                        #print "l=0"
                elif "Outputs" in line:
                    l=1 
                    k=1 #Added on 26/04/15
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
    return module

def find_sub_modules(verilog_file):
    """Find out the sub-modules in a Verilog file """
    lines = open(verilog_file, 'rt').read()
    sub_module=[]
    i=0
    with open(verilog_file)as f:
        for line in f:
            if i==1:
                """Inside the module instantiation"""    
                sub_module.append(line.split()[1])
                i=0
            elif "Module instantiation" in line:
                i=1
    return sub_module

def find_inputs_of_module(verilog_file, module_name):
    """Function to return the inputs and outputs of a module
    Inputs: The name of MUT (Add the verilog file name later)
    Outputs: Two lists inputs_test_module and outputs_test_module"""
    lines = open(verilog_file, 'rt').read()
    """ Extracting inputs and outputs of module to be tested """
    inputs_test_module = []
    outputs_test_module = []
    k = 0
    i = 0		
    with open(verilog_file)as f:
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
	""" Removing spaces in the strings 'inputs_test_module' and \
        outputs_test_module """
	rem_space (inputs_test_module)
	#print inputs_test_module
	rem_space (outputs_test_module)
	#print outputs_test_module
	return inputs_test_module, outputs_test_module

def remove_duplicates(input_list):
    """Ref: http://stackoverflow.com/questions/480214/how-do-you-remove-\
    duplicates-from-a-list-in-python-whilst-preserving-order"""
    """Function to remove duplicate entries in a list"""
    seen = set()
    seen_add = seen.add
    return [ x for x in input_list if not (x in seen or seen_add(x))]

def find_inputs_of_top_module(verilog_file_name):
    """Returns the inputs of the top module in the verilog_file_name"""
    inputs=[]
    inputs_out=[]
    f = open(verilog_file_name, 'rt')
    for line in f:
        match=re.search(r'input\s*\w+;', line)
        if match:
            inputs.append(match.group())
    """Replacements required"""
    reps = {';':'', 'input':'', ' ':''}
    for line in inputs:
        inputs_out.append(replace_all(line, reps))
    return inputs_out

def replace_all(text, dic):
    """Do the replacements to the string text as specified by the \
    dictionary dic.
    Ref:https://gomputor.wordpress.com/2008/09/27/search-replace-multiple\
    -words-or-characters-with-python/"""  
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

def find_modules_input_fan_in_cone(verilog_file, MUT):
    """Definition of some lists"""
    """Queue which contains the signals in the fan-in cone of the MUT.\
    It is changed dynamically"""
    input_queue=[]
    input_queue_traced=[]
    """Modules which come in the fan in cone of the MUT"""
    modules_required=[]
    primary_input_set=[]
    signal_module_pairs=[]
    modules_required.append(MUT)
    input_queue=find_inputs_of_module(verilog_file,MUT)[0]
    #print input_queue
    primary_inputs=find_inputs_of_top_module(verilog_file)
    #print "primary_inputs: \n",primary_inputs
    #print modules_required
    """Loop to find modules_required (which have to be retained on slicing"""
    for signal in input_queue:
        if (signal not in  input_queue_traced):
            if (signal not in  primary_inputs):
                #print "signal now is %s" %(signal)
                input_queue_traced.append(signal)
                #print "input_queue_traced"
                #print input_queue_traced
                #print "locate_modules(verilog_file,signal) = %s" %(locate_modules(verilog_file,signal))
                if(locate_modules(verilog_file,signal)!=""):
                    """If loop is to avoid blank module names"""
                    """For the purpose of plotting digraph, the signal and module driving\
                    the signal are shown as tuple (signal, module_with_signal_as_output)"""
                    signal_module_pairs.append((signal,locate_modules(verilog_file,signal)))
                    modules_required.append(locate_modules(verilog_file,signal))
                    #print remove_duplicates(modules_required)
                    for i in range(len(find_inputs_of_module(verilog_file,\
                                                                 locate_modules(verilog_file,signal))[0])):
                        input_queue.append(find_inputs_of_module\
                                               (verilog_file,locate_modules(verilog_file,signal))[0][i])
                    #remove_duplicates(input_queue)
                    """
                    print "input_queue"
                    print input_queue
                    print "input_queue_traced_latest"
                    print input_queue_traced
                    print "one iteration done"
    print"\nAll done. Yeyy!!!"
    """
    return modules_required, signal_module_pairs

def log_data():    
    """Logging warnings, error messages and useful info to a file""" 
    """use 'a' to append the log file"""
    """Overwriting the log file is not working. Try later""" 
    logging.basicConfig(
        filename='log/slice_log.txt',
        filemode='w',
        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
        datefmt='%H:%M:%S',
        level=logging.DEBUG)
    return logging

def slice_code(verilog_file, modules_to_be_sliced):
    """Removing modules_to_be_sliced"""
    k=0
    f=open(verilog_file, 'rt')
    f_sliced=open('output_files/'+verilog_file.split('.v')[0]+'_sliced'+'.v', 'w')
    for module in modules_to_be_sliced:
        for line in f:
            match=re.search(r'^\s*\w+\s%s' %(module), line)
        #match=re.search(r'\w+\s%s' %(module), line)
            if match:
                k=1
                #print match.group()
            #inputs.append(match.group())        
            if k==1:
                if (re.search(r';',line)):
                    #print line
                    k=0
            elif k==0:
                #print "k==0"
                f_sliced.write(line)
    f.close()
    f_sliced.close()

def assign_floating_signals(inputs_modules_to_be_sliced,outputs_modules_to_be_sliced,\
                                inputs_modules_required,outputs_modules_required):    
    """Reassigning the signals affected by slicing"""
    """Inputs: inputs_modules_to_be_sliced,outputs_modules_to_be_sliced,\
                                inputs_modules_required,outputs_modules_required"""
    """Output: potential_PO,potential_PI,inputs_to_be_deleted,outputs_to_be_deleted"""
    potential_PO=[]
    potential_PI=[]
    inputs_to_be_deleted=[]
    outputs_to_be_deleted=[]
    """Reassigning the inputs of MUT"""
    print "inputs_modules_to_be_sliced = %s"  %(inputs_modules_to_be_sliced)
    for s in inputs_modules_to_be_sliced:
        print "%s is an input of the modules_to_be_sliced" %(s)  
        if s in outputs_modules_required:
            if s not in inputs_modules_required:
                potential_PO.append(s)
                print "%s is not the input of any other module -> potential_PO" %(s)
            elif s in inputs_modules_required :
                print "%s is the input of some module -> NOP" %(s)
        elif s not in outputs_modules_required:
            if s not in inputs_modules_required:
                inputs_to_be_deleted.append(s)
            elif s in inputs_modules_required:
                print "%s is the input of some module -> NOP " %(s)
    print  "potential_PO=%s" %(potential_PO)
    print "inputs_to_be_deleted=%s" %(inputs_to_be_deleted)    
    """Reassigning the outputs of MUT"""
    print "outputs_modules_to_be_sliced = %s" %(outputs_modules_to_be_sliced)
    for s in outputs_modules_to_be_sliced:
        print "%s is an output of the modules_to_be_sliced" %(s)  
        if s in inputs_modules_required:
            potential_PI.append(s)
            print "%s is the input of some module -> potential_PI" %(s)
        elif s not in inputs_modules_required:
            outputs_to_be_deleted.append(s)
            print "%s is not an input of any module -> delete it " %(s)
    print  "potential_PI=%s" %(potential_PI)
    print "outputs_to_be_deleted=%s" %(outputs_to_be_deleted)        
    return (potential_PO,potential_PI,inputs_to_be_deleted,outputs_to_be_deleted)

def add_IO_pins_to_sliced_code(VERILOG_FILE_NAME,potential_PO,potential_PI,inputs_to_be_deleted,outputs_to_be_deleted):
    """Adding potential_PO & potential_PI, deleting inputs_to_be_deleted & outputs_to_be_deleted"""
    """Inputs: VERILOG_FILE_NAME,potential_PO,potential_PI,inputs_to_be_deleted,outputs_to_be_deleted"""
    """Outputs: The modified Verilog code in the directory ./output_files/"""
    i=0
    o=0
    f=open('output_files/'+VERILOG_FILE_NAME.split('.v')[0]+"_sliced"+'.v', 'rt')
    f_IO_added=open('output_files/'+VERILOG_FILE_NAME.split('.v')[0]+'_sliced_with_modified_IOports'+'.v', 'w')
    for line in f:
        if "Inputs_top" in line:
            print "Inputs_top found"
            i=1
            f_IO_added.write(line)
            for signal in potential_PI:
                f_IO_added.write("\ninput %s" %(signal))
                print "\ninput %s written" %(signal)
        elif "Outputs_top" in line:
            print "Outputs_top found"
            o=1
            f_IO_added.write(line)
            for signal in potential_PO:
                f_IO_added.write("\toutput %s;\n" %(signal))
                print "\noutput %s written" %(signal)
        elif i==1:
            print "i==%d"%(i)
            if inputs_to_be_deleted!=[]:
                for signal in inputs_to_be_deleted:
                    if ("input %s" %(signal)) in line:
                        print "input %s is deleted" %(signal)
                    elif "End of inputs_top" in line:
                        f_IO_added.write(line)
                        i=0
                    else:
                        f_IO_added.write(line)
                        print "%s written" %(line)
            else:
                if "End of inputs_top" in line:
                    f_IO_added.write(line)
                    i=0
                else:
                    f_IO_added.write(line)
                    print "%s written, inputs_to_be_deleted was null" %(line)                
        elif o==1: #WORK_never entering this loop
            print "o==%d"%(o)
            for signal in outputs_to_be_deleted:
                if ("output %s" %(signal)) in line:
                    print "output %s is deleted" %(signal)
                elif "End of outputs_top" in line:
                    f_IO_added.write(line)
                    o=0
                else:
                    f_IO_added.write(line)
                    print "%s written" %(line)
        elif i==0 and o==0:
            f_IO_added.write(line)
            print "Nothing much happened, writing the line"
    f.close()
    f_IO_added.close()

""" MAIN()"""
##############

"""Declarations"""
modules_required=[]
inputs_modules_required=[]
outputs_modules_required=[]
all_modules=[]
modules_to_be_sliced=[]
inputs_modules_to_be_sliced=[]
outputs_modules_to_be_sliced=[]

"""Logging is not updating th file: Do later"""
#logger=log_data()
#logging=log_data()
"""
logging.basicConfig(
    filename='log/slice_log.txt',
    filemode='w',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG)
logging.info("Info")
logging.error("error message")
logging.warning("warning message")
"""

"""Uncomment later"""
#MUT = raw_input ("Give the name of the module to be tested:")
#MUT="u2_half_adder"
MUT="test1"

#print find_inputs_of_top_module(VERILOG_FILE_NAME)
"""Modules which have to be retained while slicing"""
modules_required=find_modules_input_fan_in_cone(VERILOG_FILE_NAME, MUT)[0]
"""List of all sub-modules in which does port-mapping in VERILOG_FILE_NAME""" 
all_modules=find_sub_modules(VERILOG_FILE_NAME)
"""Modules which should be removed"""
modules_to_be_sliced=list(set(all_modules)-set(modules_required))
"""Find inputs of modules_required"""
for module in modules_required:
    inputs_modules_required=inputs_modules_required+find_inputs_of_module(VERILOG_FILE_NAME,module)[0]
inputs_modules_required=remove_duplicates(inputs_modules_required)
#print inputs_modules_required
"""Find inputs of modules_to_be_sliced"""
for module in modules_to_be_sliced:
    inputs_modules_to_be_sliced=inputs_modules_to_be_sliced+find_inputs_of_module(VERILOG_FILE_NAME,module)[0]
inputs_modules_to_be_sliced=remove_duplicates(inputs_modules_to_be_sliced)
#print inputs_modules_to_be_sliced
"""Find outputs of modules_required"""
for module in modules_required:
    outputs_modules_required=outputs_modules_required+find_inputs_of_module(VERILOG_FILE_NAME,module)[1]
outputs_modules_required=remove_duplicates(outputs_modules_required)
#print outputs_modules_required
"""Find outputs of modules_to_be_sliced"""
for module in modules_to_be_sliced:
    outputs_modules_to_be_sliced=outputs_modules_to_be_sliced+find_inputs_of_module(VERILOG_FILE_NAME,module)[1]
outputs_modules_to_be_sliced=remove_duplicates(outputs_modules_to_be_sliced)
#print outputs_modules_to_be_sliced
"""Removing modules_to_be_sliced"""
slice_code(VERILOG_FILE_NAME, modules_to_be_sliced)
"""Decide upon what to do with the floating signals due to slicing"""
potential_PO,potential_PI,inputs_to_be_deleted,outputs_to_be_deleted=\
    assign_floating_signals(inputs_modules_to_be_sliced,outputs_modules_to_be_sliced,\
                                inputs_modules_required,outputs_modules_required)
#print potential_PO,potential_PI,inputs_to_be_deleted,outputs_to_be_deleted
"""Adding potential_PO & potential_PI, deleting inputs_to_be_deleted & outputs_to_be_deleted"""
add_IO_pins_to_sliced_code(VERILOG_FILE_NAME,potential_PO,potential_PI,inputs_to_be_deleted,outputs_to_be_deleted)
