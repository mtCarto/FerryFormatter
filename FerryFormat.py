#!/usr/bin/python

import cmd, sys
import datetime as dt
import csv
import string
import fileinput
import itertools
import operator

class csvFormatter(cmd.Cmd):
  "Morgan's Venus csv formatter"

  def __init__(self):
    cmd.Cmd.__init__(self)
    self.intro = "Welcome to the Venus csv data formatter"
    self.prompt = "=>"

  def emptyline(self):
    pass
  
  def do_exit(self, line):
    return True

  def parseline(self, line):
    ret = cmd.Cmd.parseline(self,line)
    return ret

  def do_stripMeta(self,line):
    retype = False
    while retype is False:
      print "Stripping metadate and saving to separate file. \n"
      currDir = "./"
      workfile = raw_input('Enter the filename: ')
      workFullFile = currDir + workfile

      confirm = confirmPrompt()
      if (confirm == True):
        break

    print "Opening File"
    print workFullFile
   #error catching if file is not find or entered name is wrong 
    lines = open(workFullFile,'r').readlines()
    
    #find water property lines, or just header line
    out = open("output.txt", 'w+')
#before outputting format the header names, try using the CSV lib    
#data headers are on line 16 always, write out headers and rest of file to output.txt
    out.writelines(lines[16:])
  
  def do_prepData(self,line):
    print "Formatting data for GIS import. "
    #strip out spaces and special chars in column headers, format for input in to GIS (arc or Q)
    lines = open("./output.txt", 'r')
#load first line, iterate through line
#     find all ' , ' and replace with ','
#     find gaps in header names and replace with '_'
#     find [] and () and remove

  def do_formatData(self,line):
    print "data formatting options"
    #average data, find poor QC flags, remove desired column, etc
    #data mining tools?

  def help_stripMeta(self):
    print "Will strip the dataset metadata from the input file and save as a new metadata text file"

  def help_prepData(self):
    print "Removes spaces and inappropriate characters to prepare for GIS use"

  def help_formatData(self):
    print "Optional removal of QC Flags, etc"

#def stripMeta():
#look for % symbols and copy all strings in between into new text file  
#remove metadata, and save data as new file  

#def prepData():
#remove spaces and units from column headers for GIS import

#def formatData():
#optional functions 
#remove QC flags, convert timestamp, find data gaps and report
def confirmPrompt():
  user_conf = raw_input("Is this correct?")
  while user_conf.lower() not in {'yes','no','y','n'}:
    print "Invalid response"
    user_conf = raw_input("Is this correct?")

  if (user_conf in {'no','n'}):
    print "Starting again"
    return False
  elif (user_conf in {'yes','y'}):
    return True

def loopGroup(groupFunction):
  while True:
    groupfunction()
    staychoice = input("Repeat last action?")
    if (staychoice in {'y','yes'}):
      continue
    elif (staychoice in {'n','no'}):
      break
    else: 
      print("Please choose yes or no")

def main():
  print("Welcome to Morgan's Venus data formatter\n")
 # fileLoc = input("Enter the location of the file to be formatted: ") 
 # fileName = input("\n Enter the name of the file: ")
 # fileName = fileLoc + '/' + fileName
 # fileinput.input(fileName)

if __name__ == "__main__":
  csvFormatter().cmdloop()
#ask for file location
#open file, report if error
#strip metadata from file head
#prepData 
#formatData

#ask if loop back to start, or specific function
