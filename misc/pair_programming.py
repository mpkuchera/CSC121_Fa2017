
"""
Created on Thu Jan 12 16:53:45 2017

@author: Michelle P. Kuchera
@brief: This program randomly pairs students for in-class work and does \
        pair programming timing with vocals for the Mac.
"""

import numpy as np
import time
import os

students = ["Will Baldwin", "Mike Bauman", "Nick Boyd", "Liam Carriker", "Dimitrios Chavouzis", "Austin Craig", "Jack Dowell", \
"Nicky Emanuel", "Kyle Galla", "Madelyn Gatchel", "Anna Grumman", "Drew Hager", "Trey Harris", "Owen Keefer", "Jennifer Lee", "Tori Lindelow", "Morgan McDougal", \
"Sofia Mills", "Chris Myers", "Nick Nolting", "Julia Sirvinkas", "Eleni Tsitinidi", "Charlotte Woodhams", "John Zhou"]

print "there are", len(students), "students in the class. They are:" 
for student in students:
    print student, ",   "

students_per_group = 2 # = 2 when we are creating pairs

num_groups = len(students) / students_per_group

print "\n\nThere are",num_groups, "groups in the class."

np.random.shuffle(students)

#Print each pair and their table assignment
for i in range(0,int(num_groups)):
    print "Table ",i+1,": ",students[i*students_per_group],"and" ,students[i*students_per_group+1], " "

# if we have an extra student: add them to the last group
if(len(students)%students_per_group != 0):
    print "and" ,students[-1]

    
# The below code manages the pair programming role timing    
raw_input("\n\nPress `Enter` when ready to start pair programming:")
inp_min = input('How much time do the students have in minutes? ')
minutes = float(inp_min)
tot_time = minutes * 60
inp_turn = input('How much time is one turn in minutes?')
one_turn = float(inp_turn)*60
print "\nStart coding!"
os.system('say "Start Coding!"')
for t in range(0,int(tot_time/one_turn)):
    time.sleep(one_turn)
    print "Time to switch roles!"
    os.system('say "Switch roles!"')
    
