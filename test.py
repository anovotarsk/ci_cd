import csv
import os

def check_output( student_out_file, need_out_file ):
    student_fd = open( student_out_file, "r" )
    need_fd = open( need_out_file )
    student_out = student_fd.read()
    need_out = need_fd.read()

    student_fd.close()
    need_fd.close()

    if student_out != need_out:
        return False
    return True

os.system("pwd && ls")

file = open( "students.csv", "r" )
reader = csv.reader( file  )

students = []
repositories = []
rez = []

reader.__next__()

for row in reader:
    students.append( row[0] )
    repositories.append( row[1] )

del reader
file.close()

for i in range( len( students ) ):
    run_program = "cd " + students[i] + " && " + "g++ test.cpp && ./a.out > out"

    os.system( "git clone " + repositories[i] + " " + students[i] )
    os.system( run_program )
    check = check_output( students[i] + "/out", "need_out" )
    os.system( "rm -rf " + students[i] )
    if check == True:
        rez.append( "True" )
    else:
        rez.append( "False" )


file = open( "students.csv", "w" )

file.write( "Students,Repositories,Test\n" )
for i in range( len( students ) ):
    data = students[i] + "," + repositories[i] + "," + rez[i] + "\n"
    file.write( data )

file.close()

