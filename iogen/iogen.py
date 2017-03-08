import os
import time

# Args
generator_args = [
  (3,"foo"),
  (2,"bar"),
  (1,"baz")
]
"""
generator_args = [
  (n, arg),
  ...
]
Runs generator with argument arg n times and so on
"""

# Paths
generator = "echo"         
solver = "echo yah"        
input_dir = "Example/input"         
output_dir = "Example/output"     

# Create Inputs
if not os.path.isdir(input_dir):
    os.mkdir(input_dir)


nfiles = 1
for (times, arg) in generator_args:
    for i in range(times):
        os.system("{} {} > {}/{}.txt".format(generator, arg, input_dir, nfiles))
        time.sleep(1) # wait 1 sec before generating another input file
        print("generated {} {}".format(nfiles, arg))
        nfiles += 1
nfiles -= 1



# Create outputs
if not os.path.isdir(output_dir):
    os.mkdir(output_dir)
for i in range(1,nfiles+1):
    os.system("{} < {}/{}.txt > {}/{}.txt".format(solver, input_dir, i, output_dir, i))
    print("solved {}".format(i))

 
