import argparse # this will help create CLI elements
 
# this is the name of the parser object that will parse the commandline
parser = argparse.ArgumentParser(description="")
 
# the arguments will be coded in the following format
# parser.add_argument('--insert_name_here',nargs='?', const='bar',default=False, help='')
 
# this is the argument that concerns the name of the file that will have the list of the names of columns to be kept
parser.add_argument('--',nargs='?', const='bar',default=False, help= "")
 
# This should be the full location of the old file
parser.add_argument('--',nargs='?', const='bar',default=False, help=' ')
 
# The should be the name of the new file
parser.add_argument('--',nargs='?', const='bar',default=False, help='')
 
# unsure about the function of this one
args = parser.parse_args()
