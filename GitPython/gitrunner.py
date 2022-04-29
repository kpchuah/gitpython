#!/Users/chuahkianpang/opt/anaconda3/bin/python3

# Python program to explain os.system() method 
      
# importing os module 
import os 
  
# Command to execute
# Using Windows OS command
cmd = "git"
  
# Using os.system() method
os.system(cmd)
Lines = open("commands.txt")

for line in Lines:
    os.system(line)