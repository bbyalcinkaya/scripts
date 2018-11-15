import os
import time
import itertools
# Args
generator_args = sum((
  ("foo",)*3,
  ("bar",)*2,
  ("baz",)*1
), tuple())

# Executables
generator = "echo"         
solver = "echo yah"

# File paths
input_dir = "Example/input"         
output_dir = "Example/output"     
input_format = lambda i: f"{input_dir}/input{i}.txt"
output_format = lambda i: f"{output_dir}/output{i}.txt"

# File names
input_files = [input_format(i) for i in range(len(generator_args))]
output_files = [output_format(i) for i in range(len(generator_args))]

# Create directories
if not os.path.isdir(input_dir):
    os.makedirs(input_dir, exist_ok=True)
if not os.path.isdir(output_dir):
    os.makedirs(output_dir, exist_ok=True)


for (inp, out, arg) in zip(input_files, output_files, generator_args):
  os.system(f"{generator} {arg} > {inp}")
  print("Created Input:", inp)
  os.system(f"{solver} < {inp} > {out}")
  print("Created Output:", out)


 
