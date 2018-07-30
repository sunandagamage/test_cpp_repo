import sys

build_dir = sys.argv[1]
return_code = sys.argv[2]

# Built success case: create some output file
if return_code == 0:
	print("Build script successful")
    
	with open(build_dir + '/output_binary', "w") as output_file:
		output_file.write('Binary_content')

else:
	print("Build script failed", file=sys.stderr)


sys.exit(return_code)
