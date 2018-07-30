import sys, datetime

build_dir = sys.argv[1]
return_code = int(sys.argv[2])
timestamp = datetime.datetime.now().strftime('%Y-%m-%d__%H-%M-%S')

print("build_dir={}, return_code={}, timestamp={}".format(build_dir, return_code, timestamp))

# Built success case: create some output file
if return_code == 0:
	print("Some output - 1")
	print("Build script successful")
    
	with open(build_dir + '/output_binary_1', "w") as output_file:
		output_file.write('Binary_content_1_' + timestamp)
		
	with open(build_dir + '/output_binary_2', "w") as output_file:
		output_file.write('Binary_content_2_' + timestamp)

else:
	print("Some output - 2")
	print("Build script failed", file=sys.stderr)


sys.exit(return_code)
